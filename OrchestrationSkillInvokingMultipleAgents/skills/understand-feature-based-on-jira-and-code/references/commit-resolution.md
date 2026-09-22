# Change-set resolution

Before any code is read, the change set that implements the ticket must be pinned to a
verified diff boundary. `scripts/resolve_change_set.py` does this deterministically. Run
the script; do not reimplement its git commands by hand.

```bash
python .claude/skills/understand-feature-based-on-jira-and-code/scripts/resolve_change_set.py \
  --jira-id OMPS-1234 --json
```

Run it from the repository root. Add `--repo <path>` if you are elsewhere. Omit `--json`
to get the human-readable guard block, which is the text to paste into the artifact.

## Why a script instead of ad-hoc git

Three reasons, all learned from this repository:

- `git log --grep=OMPS-501` also matches `OMPS-5011`. The script re-checks every grep hit
  against a word-boundary pattern, so a short key cannot silently resolve to a longer
  ticket's merge.
- Branch names in this working copy do not indicate what a branch is. There are roughly
  twenty dated snapshots of master (`master9thSeptember`, `master20thAug`, `master-27thJuly`, …)
  that match no master-like naming pattern, while `feature/OMPS-4635` looks like a feature
  branch. The script classifies by graph position only.
- A dated snapshot can sit behind `origin/master`, so a commit found on the mainline may
  not exist in the checked-out tree. The script verifies containment instead of assuming it.

## Checkout modes

Mode comes from `git merge-base --is-ancestor HEAD <mainline>` plus
`git rev-list --left-right --count HEAD...<mainline>`, never from the branch name.

| Mode | Meaning | Boundary |
|---|---|---|
| `MAINLINE_TIP` | HEAD equals the mainline tip | mainline resolution rules 1–5 |
| `MAINLINE_SNAPSHOT` | HEAD is an ancestor of the mainline (a dated snapshot) | mainline resolution rules 1–5, over the snapshot's history |
| `FEATURE_BRANCH` | HEAD carries commits the mainline does not | `merge-base(mainline, HEAD)..HEAD` |

## The search ref defaults to `HEAD`

Searching `HEAD` guarantees that the resolved change set exists in the tree you are about
to read. Searching `origin/master` can resolve a landing commit whose files are not on
disk, and the resulting analysis would describe code that is not there — silently.

If the ticket landed after the snapshot date, the script reports
`LANDING_NEWER_THAN_CHECKOUT`, names the snapshot branch and how far behind it is, and
exits non-zero. Two honest ways forward: check out a ref that contains the change, or pass
`--search-ref origin/master` to opt into an off-checkout analysis. In the second case the
script sets `off_checkout: true`, caps confidence at `MEDIUM`, and the artifact must state
that the analysis describes commits not present in the working copy.

## Resolution rules

The script applies these in order and reports which one fired in `resolution_rule`.

- **Rule 1 — first-parent search** (`RULE_1_FIRST_PARENT`, confidence `HIGH`).
  `git log --first-parent --format=%H%x09%s --grep=<KEY> -i <search-ref>`. This is the
  primary strategy. It works well here because Azure DevOps writes subjects like
  `Merged PR 811635: OMPS-5011:- Add factor models to IRS request body with taxlots API`.
  A plain `git log --grep` without `--first-parent` is not an equivalent strategy: it
  returns branch-internal commits and cannot tell you where work landed.
- **Rule 2 — loose commit trace** (`RULE_2_LOOSE_TRACE`, confidence `MEDIUM`).
  `git log --no-merges --grep=<KEY> -i <search-ref>`, then for each candidate either
  classify it `ON_CHAIN` (it is itself on `git rev-list --first-parent <search-ref>`, i.e.
  a squash or direct commit) or `VIA_MERGE` and trace it with
  `git rev-list --ancestry-path --merges <sha>..<search-ref>`, taking the last entry.
  Confidence is `MEDIUM` because the key never reached the first-parent chain.
- **Rule 3 — commit shape.** `git rev-list --parents -n 1 <sha>`. Two or more parents means
  a merge, diffed `M^1..M`; otherwise a direct or squashed commit, diffed `C^..C` (empty
  tree for a root commit). This stays correct when the landing merge is the branch tip.
- **Rule 4 — boundary verification.** `git diff --name-status --find-renames`, plus
  `git rev-list --merges M^1..M^2` for branch-internal merges, plus a scan of the landed
  commit subjects for other `[A-Z]+-\d+` keys.
- **Rule 5 — fallbacks**, only on explicit request. `--pr <number>` greps
  `Merged PR <number>` on the first-parent chain (`MEDIUM`); `--symbol <identifier>`
  runs `git log -S<identifier> --first-parent` optionally narrowed by `--path` (`LOW`,
  and must be confirmed against the diff contents). Date and author searches produce
  candidates only and never resolve a change set on their own.
- `--sha <commit>` skips the search when you already know the landing commit
  (`EXPLICIT_SHA`, `HIGH`). The script notes it if that commit's subject does not mention
  the key.

## Ambiguity codes

Blocking codes force exit status 2. Stop; do not analyse code.

| Code | Blocking | Meaning |
|---|---|---|
| `NO_MATCH_ON_SEARCH_REF` | yes | Nothing on the search ref mentions the key. Ticket may be unmerged. |
| `MULTIPLE_LANDING_CANDIDATES` | yes | The key landed more than once, or traces to several landings. The boundary is a choice, not a fact. |
| `LANDING_NEWER_THAN_CHECKOUT` | yes | The landing commit is not reachable from HEAD. |
| `INTERLEAVED_JIRA_KEYS` | no | Other Jira keys appear in the landed commit subjects. The diff is still correct, but call out which changes may belong to another ticket. |
| `BRANCH_INTERNAL_MERGES` | no | The landed branch contains merge commits. Common and usually benign (mainline merged into the branch); confirm nothing unrelated rode along. |

Advisory codes appear in a resolved result. They do not stop the workflow, but they must be
reproduced under `### Ambiguities` in the artifact so downstream agents can see them.

### Clearing the two advisory codes

Neither is meant to be reported unresolved. Both can be settled with one command:

```bash
git log --format=%H%x09%P%x09%s <diff-base>..<diff-head>
```

`%P` lists each commit's parents, which is what you need:

- **`BRANCH_INTERNAL_MERGES`** — the usual case is a merge of the mainline *into* the feature
  branch. If that merge's second parent is the diff base, or an ancestor of it, the merge
  contributes nothing to the diff and the advisory is benign. Say so explicitly. A merge whose
  second parent is some other branch is the case that deserves scrutiny.
- **`INTERLEAVED_JIRA_KEYS`** — read the subjects to see which commits carry a foreign key, then
  check whether their files overlap the change set with
  `git diff --name-only <sha>^ <sha>`. Name the files that belong to the other ticket.

## Exit codes

| Code | Meaning | What to do |
|---|---|---|
| 0 | Resolved | Print the guard block, then analyse. |
| 2 | Ambiguous or unresolved | Print the guard block and stop. No code reading, no bug analysis, no QA scenarios. |
| 1 | Usage error, or git unavailable / not a repository | Report the stderr message verbatim and stop. |

## JSON fields

`--json` returns `status`, `jira_id`, `repo_root`, `current_branch`, `head_sha`,
`mainline_ref`, `base_branch`, `checkout_mode`, `ahead_of_mainline`, `behind_mainline`,
`search_ref`, `search_ref_sha`, `resolution_rule`, `landing_sha`, `landing_sha_short`,
`landing_subject`, `landing_type`, `diff_base`, `diff_head`, `diff_command`,
`feature_commit_count`, `feature_commits[]`, `changed_file_count`, `changed_files[]` (with
`status`, `path` and `old_path` for renames), `diff_stat`, `confidence`, `ambiguities[]`
(with `code`, `detail`, `blocking`), `candidates[]`, `interleaved_jira_keys[]`,
`off_checkout` and `notes[]`.

Use `diff_command` verbatim as the starting point for reading the change. For a merge that
is `git diff --find-renames <M^1> <M>`; per-file detail comes from
`git diff --find-renames <base> <head> -- <path>`.
