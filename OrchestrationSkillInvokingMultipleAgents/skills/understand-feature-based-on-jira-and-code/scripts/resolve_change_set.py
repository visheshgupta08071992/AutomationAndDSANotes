#!/usr/bin/env python3
"""Resolve the git change set that implements a Jira ticket.

Deterministic implementation of the change-set resolution rules used by the
`understand-feature-based-on-jira-and-code` workflow. The script never reads
code and never guesses: it either resolves a landing commit with a verified
diff boundary, or it reports why it could not.

Usage
-----
    python resolve_change_set.py --jira-id OMPS-5011
    python resolve_change_set.py --jira-id OMPS-5011 --json
    python resolve_change_set.py --jira-id OMPS-5011 --search-ref origin/master
    python resolve_change_set.py --jira-id OMPS-5011 --pr 811635
    python resolve_change_set.py --jira-id OMPS-5011 --symbol resolveFactorModels
    python resolve_change_set.py --jira-id OMPS-5011 --sha 8138a0cbf

Exit codes
----------
    0   change set resolved (advisory ambiguities may still be present)
    2   ambiguous or unresolved change set - callers must stop, not guess
    1   usage error, or git is unavailable / not a repository
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from typing import Any

# Hash of git's canonical empty tree, used as the diff base for a root commit.
EMPTY_TREE = "4b825dc642cb6eb9a060e54bf8d69288fbee4904"

# Candidate mainline refs, in preference order.
MAINLINE_CANDIDATES = ("origin/master", "origin/main", "master", "main")

# Fixed ambiguity code set. Blocking codes force exit status 2.
BLOCKING_CODES = frozenset(
    {
        "MULTIPLE_LANDING_CANDIDATES",
        "LANDING_NEWER_THAN_CHECKOUT",
        "NO_MATCH_ON_SEARCH_REF",
    }
)
ADVISORY_CODES = frozenset({"INTERLEAVED_JIRA_KEYS", "BRANCH_INTERNAL_MERGES"})

JIRA_KEY_RE = re.compile(r"\b[A-Z][A-Z0-9]+-\d+\b")

CONFIDENCE_ORDER = ("UNRESOLVED", "LOW", "MEDIUM", "HIGH")


class GitError(RuntimeError):
    """A git invocation failed in a way the caller cannot recover from."""


class UsageError(RuntimeError):
    """The arguments or repository state make resolution impossible."""


@dataclass
class Result:
    """Everything the workflow's change-set resolution guard needs to report."""

    jira_id: str
    repo_root: str = ""
    current_branch: str = ""
    head_sha: str = ""
    mainline_ref: str = ""
    checkout_mode: str = ""
    ahead_of_mainline: int = 0
    behind_mainline: int = 0
    search_ref: str = ""
    search_ref_sha: str = ""
    resolution_rule: str = ""
    landing_sha: str = ""
    landing_subject: str = ""
    landing_type: str = ""
    diff_base: str = ""
    diff_head: str = ""
    feature_commits: list[dict[str, str]] = field(default_factory=list)
    changed_files: list[dict[str, str]] = field(default_factory=list)
    diff_stat: dict[str, int] = field(default_factory=dict)
    confidence: str = "UNRESOLVED"
    ambiguities: list[dict[str, Any]] = field(default_factory=list)
    candidates: list[dict[str, str]] = field(default_factory=list)
    interleaved_jira_keys: list[str] = field(default_factory=list)
    off_checkout: bool = False
    notes: list[str] = field(default_factory=list)

    # -- mutation helpers -------------------------------------------------

    def add_ambiguity(self, code: str, detail: str) -> None:
        if code not in BLOCKING_CODES and code not in ADVISORY_CODES:
            raise ValueError(f"unknown ambiguity code: {code}")
        self.ambiguities.append(
            {"code": code, "detail": detail, "blocking": code in BLOCKING_CODES}
        )

    def cap_confidence(self, level: str) -> None:
        if CONFIDENCE_ORDER.index(level) < CONFIDENCE_ORDER.index(self.confidence):
            self.confidence = level

    # -- derived values ---------------------------------------------------

    @property
    def blocking_ambiguities(self) -> list[dict[str, Any]]:
        return [a for a in self.ambiguities if a["blocking"]]

    @property
    def status(self) -> str:
        if not self.landing_sha:
            return "UNRESOLVED"
        return "AMBIGUOUS" if self.blocking_ambiguities else "RESOLVED"

    @property
    def exit_code(self) -> int:
        return 0 if self.status == "RESOLVED" else 2

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "jira_id": self.jira_id,
            "repo_root": self.repo_root,
            "current_branch": self.current_branch,
            "head_sha": self.head_sha,
            "head_sha_short": self.head_sha[:9],
            "mainline_ref": self.mainline_ref,
            "base_branch": self.mainline_ref,
            "checkout_mode": self.checkout_mode,
            "ahead_of_mainline": self.ahead_of_mainline,
            "behind_mainline": self.behind_mainline,
            "search_ref": self.search_ref,
            "search_ref_sha": self.search_ref_sha,
            "resolution_rule": self.resolution_rule,
            "landing_sha": self.landing_sha,
            "landing_sha_short": self.landing_sha[:9],
            "landing_subject": self.landing_subject,
            "landing_type": self.landing_type,
            "diff_base": self.diff_base,
            "diff_head": self.diff_head,
            "diff_command": self.diff_command,
            "feature_commit_count": len(self.feature_commits),
            "feature_commits": self.feature_commits,
            "changed_file_count": len(self.changed_files),
            "changed_files": self.changed_files,
            "diff_stat": self.diff_stat,
            "confidence": self.confidence,
            "ambiguities": self.ambiguities,
            "candidates": self.candidates,
            "interleaved_jira_keys": self.interleaved_jira_keys,
            "off_checkout": self.off_checkout,
            "notes": self.notes,
        }

    @property
    def diff_command(self) -> str:
        if not self.diff_base or not self.diff_head:
            return ""
        return f"git diff --find-renames {self.diff_base[:9]} {self.diff_head[:9]}"


# ---------------------------------------------------------------------------
# git plumbing
# ---------------------------------------------------------------------------


class Git:
    def __init__(self, cwd: str) -> None:
        self.cwd = cwd
        self._first_parent_cache: dict[str, set[str]] = {}

    def run(self, *args: str, check: bool = True) -> str:
        proc = subprocess.run(
            ["git", *args],
            cwd=self.cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        if check and proc.returncode != 0:
            raise GitError(
                f"`git {' '.join(args)}` failed ({proc.returncode}): "
                f"{proc.stderr.strip() or proc.stdout.strip()}"
            )
        return proc.stdout.strip()

    def ok(self, *args: str) -> bool:
        """Run a git command purely for its exit status."""
        proc = subprocess.run(
            ["git", *args],
            cwd=self.cwd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        return proc.returncode == 0

    def lines(self, *args: str) -> list[str]:
        out = self.run(*args)
        return [line for line in out.splitlines() if line.strip()]

    def rev_parse(self, ref: str) -> str:
        return self.run("rev-parse", "--verify", f"{ref}^{{commit}}")

    def ref_exists(self, ref: str) -> bool:
        return self.ok("rev-parse", "--verify", "--quiet", f"{ref}^{{commit}}")

    def log_subjects(self, *args: str) -> list[tuple[str, str]]:
        """Return (sha, subject) pairs for a `git log` invocation."""
        pairs: list[tuple[str, str]] = []
        for line in self.lines("log", "--format=%H%x09%s", *args):
            sha, _, subject = line.partition("\t")
            pairs.append((sha, subject))
        return pairs

    def is_ancestor(self, ancestor: str, descendant: str) -> bool:
        return self.ok("merge-base", "--is-ancestor", ancestor, descendant)

    def parents(self, sha: str) -> list[str]:
        return self.run("rev-list", "--parents", "-n", "1", sha).split()[1:]

    def subject(self, sha: str) -> str:
        return self.run("log", "-1", "--format=%s", sha)

    def on_first_parent_chain(self, sha: str, ref: str) -> bool:
        if ref not in self._first_parent_cache:
            self._first_parent_cache[ref] = set(
                self.lines("rev-list", "--first-parent", ref)
            )
        return sha in self._first_parent_cache[ref]


# ---------------------------------------------------------------------------
# resolution
# ---------------------------------------------------------------------------


def key_matcher(jira_id: str) -> re.Pattern[str]:
    """Match the Jira key without matching a longer key that starts the same.

    `--grep=OMPS-501` also matches `OMPS-5011`, so every git-side grep hit is
    re-checked against this pattern before it is treated as a candidate.
    """
    return re.compile(
        rf"(?<![0-9A-Za-z]){re.escape(jira_id)}(?![0-9])", re.IGNORECASE
    )


def detect_mainline_ref(git: Git, explicit: str | None) -> str:
    if explicit:
        if not git.ref_exists(explicit):
            raise UsageError(f"mainline ref does not exist: {explicit}")
        return explicit
    for ref in MAINLINE_CANDIDATES:
        if git.ref_exists(ref):
            return ref
    raise UsageError(
        "could not find a mainline ref (tried "
        + ", ".join(MAINLINE_CANDIDATES)
        + "); pass --mainline-ref"
    )


def detect_checkout_mode(git: Git, result: Result) -> None:
    """Classify HEAD relative to the mainline, ignoring branch names.

    Branch names lie in this repo: `master9thSeptember` is a snapshot of master
    and `feature/OMPS-4635` is not. Only the commit graph is trusted.
    """
    counts = git.run(
        "rev-list", "--left-right", "--count", f"HEAD...{result.mainline_ref}"
    ).split()
    result.ahead_of_mainline = int(counts[0])
    result.behind_mainline = int(counts[1])

    if not git.is_ancestor("HEAD", result.mainline_ref):
        result.checkout_mode = "FEATURE_BRANCH"
    elif result.behind_mainline == 0:
        result.checkout_mode = "MAINLINE_TIP"
    else:
        result.checkout_mode = "MAINLINE_SNAPSHOT"


def describe_landing(git: Git, result: Result) -> None:
    """Rule 3 - determine commit shape and therefore the diff boundary."""
    parents = git.parents(result.landing_sha)
    result.landing_subject = git.subject(result.landing_sha)

    if len(parents) >= 2:
        result.landing_type = "MERGE"
        result.diff_base = parents[0]
        result.diff_head = result.landing_sha
        if len(parents) > 2:
            result.notes.append(
                f"octopus merge with {len(parents)} parents; diff uses the "
                "first parent as base"
            )
    else:
        result.landing_type = "DIRECT"
        result.diff_base = parents[0] if parents else EMPTY_TREE
        result.diff_head = result.landing_sha
        if not parents:
            result.notes.append("root commit; diff base is the empty tree")


def collect_boundary(git: Git, result: Result) -> None:
    """Rule 4 - enumerate the changed files, feature commits and interleaving."""
    result.changed_files = changed_files(git, result.diff_base, result.diff_head)
    result.diff_stat = diff_stat(git, result.diff_base, result.diff_head)

    if result.landing_type == "MERGE":
        parents = git.parents(result.landing_sha)
        span = f"{parents[0]}..{parents[1]}"
        result.feature_commits = [
            {"sha": sha, "short_sha": sha[:9], "subject": subject}
            for sha, subject in git.log_subjects("--no-merges", span)
        ]
        internal_merges = git.lines("rev-list", "--merges", span)
        if internal_merges:
            result.add_ambiguity(
                "BRANCH_INTERNAL_MERGES",
                f"{len(internal_merges)} merge commit(s) inside the landed "
                f"branch ({span}); verify no unrelated work rode along",
            )
    else:
        result.feature_commits = [
            {
                "sha": result.landing_sha,
                "short_sha": result.landing_sha[:9],
                "subject": result.landing_subject,
            }
        ]

    matcher = key_matcher(result.jira_id)
    foreign: set[str] = set()
    for commit in result.feature_commits:
        for found in JIRA_KEY_RE.findall(commit["subject"]):
            if not matcher.fullmatch(found):
                foreign.add(found)
    result.interleaved_jira_keys = sorted(foreign)
    if foreign:
        result.add_ambiguity(
            "INTERLEAVED_JIRA_KEYS",
            "other Jira keys appear in the landed commit subjects: "
            + ", ".join(sorted(foreign)),
        )


def changed_files(git: Git, base: str, head: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for line in git.lines(
        "diff", "--name-status", "--find-renames", base, head
    ):
        parts = line.split("\t")
        status = parts[0]
        if status.startswith(("R", "C")) and len(parts) >= 3:
            entries.append(
                {"status": status, "path": parts[2], "old_path": parts[1]}
            )
        else:
            entries.append({"status": status, "path": parts[-1], "old_path": ""})
    return entries


def diff_stat(git: Git, base: str, head: str) -> dict[str, int]:
    out = git.run("diff", "--shortstat", "--find-renames", base, head)
    stat = {"files": 0, "insertions": 0, "deletions": 0}
    for value, keyword in re.findall(r"(\d+) (files?|insertions?|deletions?)", out):
        if keyword.startswith("file"):
            stat["files"] = int(value)
        elif keyword.startswith("insertion"):
            stat["insertions"] = int(value)
        else:
            stat["deletions"] = int(value)
    return stat


def verify_containment(git: Git, result: Result, search_ref_explicit: bool) -> None:
    """The resolved commit must be in the tree the agent will actually read.

    A dated snapshot branch can sit behind the mainline, so a commit found on
    `origin/master` may not exist on disk. Analysing that diff would silently
    describe files the working copy does not have.
    """
    if git.is_ancestor(result.landing_sha, "HEAD"):
        return

    result.off_checkout = True
    detail = (
        f"landing commit {result.landing_sha[:9]} is not reachable from HEAD "
        f"({result.current_branch} @ {result.head_sha[:9]}, {result.behind_mainline} "
        f"commit(s) behind {result.mainline_ref}); the working copy does not "
        "contain this change"
    )
    if search_ref_explicit:
        # The caller opted into an off-checkout search ref deliberately.
        result.notes.append(detail + " - analysis is off-checkout")
        result.cap_confidence("MEDIUM")
    else:
        result.add_ambiguity("LANDING_NEWER_THAN_CHECKOUT", detail)
        result.cap_confidence("LOW")


def resolve_feature_branch(git: Git, result: Result) -> None:
    """Feature-branch mode - the boundary is merge-base(mainline, HEAD)..HEAD."""
    base = git.run("merge-base", result.mainline_ref, "HEAD")
    result.resolution_rule = "FEATURE_BRANCH_MERGE_BASE"
    result.landing_sha = result.head_sha
    result.landing_subject = git.subject(result.head_sha)
    result.landing_type = "FEATURE_BRANCH"
    result.diff_base = base
    result.diff_head = result.head_sha
    result.changed_files = changed_files(git, base, result.head_sha)
    result.diff_stat = diff_stat(git, base, result.head_sha)
    result.feature_commits = [
        {"sha": sha, "short_sha": sha[:9], "subject": subject}
        for sha, subject in git.log_subjects("--no-merges", f"{base}..HEAD")
    ]

    internal_merges = git.lines("rev-list", "--merges", f"{base}..HEAD")
    if internal_merges:
        result.add_ambiguity(
            "BRANCH_INTERNAL_MERGES",
            f"{len(internal_merges)} merge commit(s) between the merge-base and "
            "HEAD (typically mainline merged into the branch)",
        )

    matcher = key_matcher(result.jira_id)
    mentions = [c for c in result.feature_commits if matcher.search(c["subject"])]
    foreign = sorted(
        {
            found
            for c in result.feature_commits
            for found in JIRA_KEY_RE.findall(c["subject"])
            if not matcher.fullmatch(found)
        }
    )
    result.interleaved_jira_keys = foreign
    if foreign:
        result.add_ambiguity(
            "INTERLEAVED_JIRA_KEYS",
            "other Jira keys appear in the branch commit subjects: "
            + ", ".join(foreign),
        )

    if mentions:
        result.confidence = "HIGH"
        result.notes.append(
            f"{len(mentions)} of {len(result.feature_commits)} branch commit(s) "
            f"mention {result.jira_id}"
        )
    else:
        result.confidence = "LOW"
        result.add_ambiguity(
            "NO_MATCH_ON_SEARCH_REF",
            f"no commit between {base[:9]} and HEAD mentions {result.jira_id}; "
            "the checked-out branch may not be this ticket's branch",
        )


def resolve_rule_1(git: Git, result: Result) -> str | None:
    """Rule 1 - first-parent search. The primary landing-point strategy."""
    matcher = key_matcher(result.jira_id)
    hits = [
        (sha, subject)
        for sha, subject in git.log_subjects(
            "--first-parent", f"--grep={result.jira_id}", "-i", result.search_ref
        )
        if matcher.search(subject)
    ]
    if not hits:
        return None

    result.candidates = [
        {"sha": sha, "short_sha": sha[:9], "subject": subject, "source": "RULE_1"}
        for sha, subject in hits
    ]
    result.resolution_rule = "RULE_1_FIRST_PARENT"
    if len(hits) > 1:
        result.add_ambiguity(
            "MULTIPLE_LANDING_CANDIDATES",
            f"{len(hits)} first-parent commits mention {result.jira_id}: "
            + "; ".join(f"{sha[:9]} {subject}" for sha, subject in hits),
        )
        result.confidence = "LOW"
    else:
        result.confidence = "HIGH"
    return hits[0][0]


def resolve_rule_2(git: Git, result: Result) -> str | None:
    """Rule 2 - loose commit search, then trace each candidate to its landing."""
    matcher = key_matcher(result.jira_id)
    hits = [
        (sha, subject)
        for sha, subject in git.log_subjects(
            "--no-merges", f"--grep={result.jira_id}", "-i", result.search_ref
        )
        if matcher.search(subject)
    ]
    if not hits:
        return None

    landings: dict[str, dict[str, str]] = {}
    for sha, subject in hits:
        if git.on_first_parent_chain(sha, result.search_ref):
            reachability, landing = "ON_CHAIN", sha
        else:
            merges = git.lines(
                "rev-list",
                "--ancestry-path",
                "--merges",
                f"{sha}..{result.search_ref}",
            )
            if not merges:
                result.notes.append(
                    f"{sha[:9]} is reachable from {result.search_ref} but has no "
                    "merge on its ancestry path; skipped"
                )
                continue
            reachability, landing = "VIA_MERGE", merges[-1]
        result.candidates.append(
            {
                "sha": sha,
                "short_sha": sha[:9],
                "subject": subject,
                "source": "RULE_2",
                "reachability": reachability,
                "landing_sha": landing,
            }
        )
        landings.setdefault(landing, {"sha": landing, "subject": git.subject(landing)})

    if not landings:
        return None

    result.resolution_rule = "RULE_2_LOOSE_TRACE"
    if len(landings) > 1:
        result.add_ambiguity(
            "MULTIPLE_LANDING_CANDIDATES",
            f"{len(hits)} commit(s) mentioning {result.jira_id} trace to "
            f"{len(landings)} distinct landings: "
            + "; ".join(f"{v['sha'][:9]} {v['subject']}" for v in landings.values()),
        )
        result.confidence = "LOW"
    else:
        # Rule 2 is a fallback: the key never reached the first-parent chain.
        result.confidence = "MEDIUM"
    return next(iter(landings))


def resolve_rule_5_pr(git: Git, result: Result, pr: str) -> str | None:
    hits = git.log_subjects(
        "--first-parent", f"--grep=Merged PR {pr}", result.search_ref
    )
    if not hits:
        return None
    result.candidates = [
        {"sha": sha, "short_sha": sha[:9], "subject": subject, "source": "RULE_5_PR"}
        for sha, subject in hits
    ]
    result.resolution_rule = "RULE_5_PR_NUMBER"
    if len(hits) > 1:
        result.add_ambiguity(
            "MULTIPLE_LANDING_CANDIDATES",
            f"{len(hits)} first-parent commits mention PR {pr}",
        )
        result.confidence = "LOW"
    else:
        result.confidence = "MEDIUM"
    result.notes.append(
        f"resolved by PR number {pr}, not by Jira key; confirm the PR belongs "
        f"to {result.jira_id}"
    )
    return hits[0][0]


def resolve_rule_5_symbol(
    git: Git, result: Result, symbol: str, path: str | None
) -> str | None:
    args = ["--first-parent", f"-S{symbol}", result.search_ref]
    if path:
        args += ["--", path]
    hits = git.log_subjects(*args)
    if not hits:
        return None
    result.candidates = [
        {
            "sha": sha,
            "short_sha": sha[:9],
            "subject": subject,
            "source": "RULE_5_SYMBOL",
        }
        for sha, subject in hits
    ]
    result.resolution_rule = "RULE_5_SYMBOL_SEARCH"
    if len(hits) > 1:
        result.add_ambiguity(
            "MULTIPLE_LANDING_CANDIDATES",
            f"{len(hits)} first-parent commits changed occurrences of "
            f"'{symbol}': "
            + "; ".join(f"{sha[:9]} {subject}" for sha, subject in hits),
        )
    result.confidence = "LOW"
    result.notes.append(
        f"resolved by symbol search for '{symbol}'; this is a weak signal and "
        "must be confirmed against the diff contents"
    )
    return hits[0][0]


def diagnose_missing(git: Git, result: Result) -> None:
    """Nothing on the search ref - say why, and whether the mainline has it."""
    detail = (
        f"no commit mentioning {result.jira_id} on {result.search_ref} "
        f"({result.search_ref_sha[:9]})"
    )
    if result.search_ref != result.mainline_ref:
        matcher = key_matcher(result.jira_id)
        elsewhere = [
            (sha, subject)
            for sha, subject in git.log_subjects(
                "--first-parent",
                f"--grep={result.jira_id}",
                "-i",
                result.mainline_ref,
            )
            if matcher.search(subject)
        ]
        if elsewhere:
            sha, subject = elsewhere[0]
            result.add_ambiguity(
                "LANDING_NEWER_THAN_CHECKOUT",
                f"{detail}, but {result.mainline_ref} has {sha[:9]} "
                f"({subject}). The checkout {result.current_branch} is "
                f"{result.behind_mainline} commit(s) behind {result.mainline_ref}, "
                f"so this ticket landed after the snapshot. Re-run with "
                f"--search-ref {result.mainline_ref} to analyse it off-checkout, "
                "or check out a ref that contains the change.",
            )
            result.confidence = "UNRESOLVED"
            return
    result.add_ambiguity(
        "NO_MATCH_ON_SEARCH_REF",
        detail
        + ". Confirm the ticket is merged, or supply --pr / --symbol / --sha.",
    )
    result.confidence = "UNRESOLVED"


def resolve(git: Git, args: argparse.Namespace, result: Result) -> None:
    result.repo_root = git.run("rev-parse", "--show-toplevel")
    result.current_branch = git.run("rev-parse", "--abbrev-ref", "HEAD")
    result.head_sha = git.rev_parse("HEAD")
    result.mainline_ref = detect_mainline_ref(git, args.mainline_ref)
    detect_checkout_mode(git, result)

    # HEAD is the default search ref so the resolved diff always matches the
    # files on disk. See verify_containment.
    search_ref_explicit = args.search_ref is not None
    result.search_ref = args.search_ref or "HEAD"
    if not git.ref_exists(result.search_ref):
        raise UsageError(f"search ref does not exist: {result.search_ref}")
    result.search_ref_sha = git.rev_parse(result.search_ref)

    if args.sha:
        result.landing_sha = git.rev_parse(args.sha)
        result.resolution_rule = "EXPLICIT_SHA"
        result.confidence = "HIGH"
        matcher = key_matcher(result.jira_id)
        if not matcher.search(git.subject(result.landing_sha)):
            result.notes.append(
                f"the subject of {result.landing_sha[:9]} does not mention "
                f"{result.jira_id}; the commit was supplied explicitly"
            )
    elif result.checkout_mode == "FEATURE_BRANCH":
        resolve_feature_branch(git, result)
        verify_containment(git, result, search_ref_explicit)
        return
    else:
        landing = resolve_rule_1(git, result)
        if landing is None:
            landing = resolve_rule_2(git, result)
        if landing is None and args.pr:
            landing = resolve_rule_5_pr(git, result, args.pr)
        if landing is None and args.symbol:
            landing = resolve_rule_5_symbol(git, result, args.symbol, args.path)
        if landing is None:
            diagnose_missing(git, result)
            return
        result.landing_sha = landing

    describe_landing(git, result)
    verify_containment(git, result, search_ref_explicit or bool(args.sha))
    collect_boundary(git, result)


# ---------------------------------------------------------------------------
# reporting
# ---------------------------------------------------------------------------


def guard_block(result: Result) -> str:
    """The change-set resolution guard block, ready to paste into an artifact."""
    lines = [
        "Change-Set Resolution Guard",
        "===========================",
        f"Jira ID:               {result.jira_id}",
        f"Current branch:        {result.current_branch} @ {result.head_sha[:9]}",
        f"Base branch:           {result.mainline_ref}",
        f"Checkout mode:         {result.checkout_mode} "
        f"(ahead {result.ahead_of_mainline}, behind {result.behind_mainline})",
        f"Search ref:            {result.search_ref} @ {result.search_ref_sha[:9]}",
        "",
        f"Resolution rule:       {result.resolution_rule or '(none)'}",
        f"Landing SHA:           {result.landing_sha[:9] or '(unresolved)'}",
        f"Landing subject:       {result.landing_subject or '(unresolved)'}",
        f"Landing type:          {result.landing_type or '(unresolved)'}",
        "",
        f"Diff base:             {result.diff_base[:9] or '(unresolved)'}",
        f"Diff head:             {result.diff_head[:9] or '(unresolved)'}",
        f"Diff command:          {result.diff_command or '(unresolved)'}",
        "",
        f"Feature commit count:  {len(result.feature_commits)}",
        f"Changed file count:    {len(result.changed_files)}",
        f"Insertions/deletions:  +{result.diff_stat.get('insertions', 0)}"
        f"/-{result.diff_stat.get('deletions', 0)}",
        f"Off-checkout:          {'yes' if result.off_checkout else 'no'}",
        "",
        f"Confidence:            {result.confidence}",
        f"Status:                {result.status}",
    ]

    if result.ambiguities:
        lines.append("Ambiguities:")
        for item in result.ambiguities:
            marker = "BLOCKING" if item["blocking"] else "advisory"
            lines.append(f"  - [{marker}] {item['code']}: {item['detail']}")
    else:
        lines.append("Ambiguities:           none")

    if result.notes:
        lines.append("Notes:")
        lines.extend(f"  - {note}" for note in result.notes)

    if result.candidates and result.status != "RESOLVED":
        lines.append("Candidates:")
        for candidate in result.candidates:
            lines.append(
                f"  - {candidate['short_sha']} [{candidate['source']}] "
                f"{candidate['subject']}"
            )

    if result.changed_files:
        lines.append("")
        lines.append(f"Changed files ({len(result.changed_files)}):")
        for entry in result.changed_files:
            rename = f" (was {entry['old_path']})" if entry["old_path"] else ""
            lines.append(f"  {entry['status']:<5} {entry['path']}{rename}")

    if result.feature_commits:
        lines.append("")
        lines.append(f"Feature commits ({len(result.feature_commits)}):")
        for commit in result.feature_commits:
            lines.append(f"  {commit['short_sha']} {commit['subject']}")

    if result.status != "RESOLVED":
        lines += [
            "",
            "STOP. The change set is not unambiguously resolved. Do not read "
            "code, do not analyse bugs, do not design QA scenarios from a "
            "guessed boundary.",
        ]

    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Resolve the git change set that implements a Jira ticket.",
    )
    parser.add_argument("--jira-id", required=True, help="e.g. OMPS-5011")
    parser.add_argument(
        "--search-ref",
        help="ref to search for the landing commit (default: HEAD, which "
        "guarantees the resolved diff matches the working copy)",
    )
    parser.add_argument(
        "--mainline-ref",
        help=f"mainline ref (default: first existing of {', '.join(MAINLINE_CANDIDATES)})",
    )
    parser.add_argument("--sha", help="explicit landing commit, skipping the search")
    parser.add_argument("--pr", help="Rule 5 fallback: pull request number")
    parser.add_argument("--symbol", help="Rule 5 fallback: identifier for `git log -S`")
    parser.add_argument("--path", help="pathspec limiting the --symbol search")
    parser.add_argument("--repo", default=os.getcwd(), help="repository path")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    jira_id = args.jira_id.strip().upper()
    if not re.fullmatch(r"[A-Z][A-Z0-9]+-\d+", jira_id):
        print(
            f"error: '{args.jira_id}' is not a Jira key (expected e.g. OMPS-5011)",
            file=sys.stderr,
        )
        return 1

    result = Result(jira_id=jira_id)
    git = Git(args.repo)
    try:
        if not git.ok("rev-parse", "--git-dir"):
            raise UsageError(f"not a git repository: {args.repo}")
        resolve(git, args, result)
    except (GitError, UsageError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
    else:
        print(guard_block(result))
    return result.exit_code


if __name__ == "__main__":
    sys.exit(main())
