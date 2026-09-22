# Shared rules

Every agent in the `understand-feature-based-on-jira-and-code` workflow reads this file
first. These rules override any instinct to be helpful by filling gaps.

## Accuracy rules

1. Never guess.
2. Never fabricate Jira requirements.
3. Never fabricate git history.
4. Never fabricate code behaviour.
5. Never fabricate review comments or PR discussion.
6. Never fabricate bugs.
7. Never fabricate test results. You do not run tests in this workflow; you read them.
8. Clearly distinguish facts from assumptions.
9. Clearly distinguish confirmed defects from potential concerns.
10. Do not treat ambiguous git history as a resolved change set.
11. Preserve the evidence and artifacts produced by earlier stages. Never delete or
    rewrite another agent's artifact.
12. Jira is the source of truth for stated requirements.
13. The local git repository is the source of truth for what changed.
14. The actual codebase is the source of truth for how the implementation behaves.
15. The identified implementation, not the Jira text alone, drives QA scenarios.
16. Do not let one incorrect assumption propagate silently downstream. If an upstream
    artifact looks wrong, say so in your own artifact instead of quietly working around it.
17. When evidence is insufficient, state that it is insufficient.
18. Prefer stopping, or reporting uncertainty, over producing a confident wrong answer.

## Sourcing discipline

Every non-obvious statement must be attributable. Use these conventions consistently:

- **Jira fact** — quote or closely paraphrase Jira text.
- **Code fact** — cite `path/to/File.java:123` or `path/to/File.java#methodName`.
- **Git fact** — cite a SHA.
- **Inference** — mark it `(inference)` and say what it is inferred from.
- **Assumption** — mark it `(assumption)` and say what would confirm or refute it.

Inferences and assumptions never appear in a section that is supposed to hold facts.
`## Functional Requirements` and `## Acceptance Criteria` in the Jira artifact are
facts-only sections; anything derived goes under `## Assumptions and Inferences`.

## Citing evidence

Cite repository-relative POSIX paths (`portfolio-service/src/main/java/...`), not absolute
Windows paths, so the artifacts stay readable and greppable for everyone. The shell here is
PowerShell and most tools return backslashes, so converting them is expected work.

Pick the citation form that stays valid as the file changes:

- **Java** — `path/File.java:123` for a specific line, or `path/File.java#methodName` when the
  method is the point. Prefer the method form; line numbers drift.
- **YAML, OpenAPI specs, generator config** — an anchor path rather than a line number, for
  example `api-schema/portfolios-v3.yaml#components.parameters.FactorModels`. These files run to
  thousands of lines and shift with every edit, so line numbers are close to useless.
- **SQL and stored procedures** — the changelog or procedure file path plus the procedure name.
- **Git** — a SHA, short form is fine.

## When an upstream artifact is missing

`agent-artifacts/` is gitignored, which means `git clean -fdx` deletes it and a long-running
workflow can lose its earlier stages' output between runs. Do not assume an artifact exists
because you were told it does.

If an upstream artifact you were given is not readable:

1. Say so immediately and name the path. Do not silently continue as though you had read it.
2. Reconstruct the minimum you need from the sources of truth, rather than stopping or guessing.
   Jira requirements come from the Atlassian connector; the change set comes from the resolver
   script and git. This is slower and gives you less than the artifact would, which is exactly
   why it must be reported.
3. Record the substitution prominently in your own artifact — for Agent 3 under
   `## Review Coverage`, for Agent 4 under `## Coverage Notes` — stating which artifact was
   missing and what you used instead.
4. Treat identifiers such as `AC-n`, `AC-D n` and `FR-n` as unavailable if Agent 1's artifact is
   gone. Do not invent your own and present them as though they came from Stage 1; number any
   you derive distinctly and say they are yours.

A missing artifact is a degraded run, not a failed one. Say which it was.

## Working with the shell

Shell startup on this machine costs roughly a minute per invocation, so a chain of small
commands is expensive. The instinct to batch many commands into one call runs into the opposite
constraint: broad or compound commands get flagged for manual approval and cost a round trip.

Prefer one narrow, single-purpose command per call, and prefer reading files with file tools over
shelling out. Note also that file-search tools respect ignore rules, so nothing under
`agent-artifacts/` will appear in their results — read those paths directly.

## Writing artifacts

- Write exactly the artifact your agent owns, at exactly the path you were given.
- Keep the prescribed headings, in the prescribed order, even when a section is empty —
  write `None identified.` rather than deleting the heading. The orchestrator gate checks
  for these headings.
- Start the artifact with an H1 that contains the Jira key.
- Aim for a focused artifact. Downstream agents must read the whole thing, so prefer
  precise citations over pasted code. Quote at most a handful of lines when the exact
  code matters; otherwise cite the location.

## Scope discipline

This workflow is read-only with respect to the codebase. No agent modifies, formats or
builds repository source, and no agent commits, stages, pushes or checks out anything. The
only writes are the artifacts under `agent-artifacts/<JIRA-ID>/` and, for Agent 4, one
Jira comment.

**Do not attempt to build or run tests.** Builds in this repository are not offline-capable:
they resolve Azure Artifacts feeds, pull secrets from Azure Key Vault, and many tasks depend on
a docker login that needs Docker Desktop running. A `./gradlew` invocation here will typically
burn several minutes and then fail on credentials, which tells you nothing about the code.

The consequence is that every statement about test coverage comes from **reading** tests, not
from running them, and each artifact must say so. That is a limitation to state plainly, not to
apologise for or work around.
