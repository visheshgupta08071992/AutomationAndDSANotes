---
name: understand-feature-based-on-jira-and-code
description: End-to-end feature understanding and QA workflow for a Jira ticket. Reads the Jira issue, resolves the implementing change set in local git, reviews the implementation for introduced defects, derives QA test scenarios, and posts them as a Jira comment. Trigger on "QA analysis for OMPS-1234", "understand feature OMPS-1234", "what changed for OMPS-1234", "find bugs introduced by OMPS-1234", "prep QA context".
---

# Understand feature based on Jira and code

Orchestrate four specialised subagents to turn a Jira key into four things: what the feature
is supposed to do, how it was implemented, what defects the implementation may have
introduced, and what QA must test.

You coordinate. You do not analyse. Do not read the Jira issue yourself, do not resolve git
history yourself, do not review code yourself and do not write test scenarios yourself — the
subagents own that work and their artifacts are the deliverables. Your job is input
validation, sequencing, gate checks and an honest final report.

## Step 1 — Validate input and prepare

Extract the Jira key from the request. Validate it against `^[A-Z][A-Z0-9]+-\d+$`, upper-casing
it first. A bare number (`5011`) defaults to the `OMPS` project, so it becomes `OMPS-5011`. If
no key can be determined, ask for one and stop; do not pick a ticket.

Create the artifact directory at the repository root:

```text
agent-artifacts/<JIRA-ID>/
```

It is gitignored. Note the absolute path — every subagent prompt passes absolute paths so no
subagent has to guess where anything lives.

If artifacts from a previous run already exist, say so and continue: each agent overwrites the
one file it owns, and Agent 4's Jira comment updates in place rather than duplicating.

### If the four subagents are not available

The four subagent types live in `.claude/agents/`. They are discovered when the session
starts, so they are unavailable if they were created during this session, and delegation can
also be blocked when this skill is itself running inside a subagent (a subagent launched by
another subagent cannot launch further subagents) or by a tool policy.

When a `Task` call cannot be made, do not abandon the workflow and do not collapse the four
stages into one pass of your own. Run each stage inline instead: read
`.claude/agents/<agent-name>.md`, follow it as your instructions for that stage only,
write that stage's artifact, then apply the gate before moving on. Preserve the boundaries
that matter — the stage order, every gate, and the rule that the QA stage never reads
`bug-analysis.md`. Note in the final report that the stages ran inline rather than as
subagents, because a single context reasoning about all four stages is more prone to
carrying an assumption across them than four isolated ones are.

## Step 2 — Agent 1, Jira understanding

One `Task` call, `subagent_type: understand-feature-based-on-jira`. Pass the Jira key and the
absolute output path `<artifacts>/jira-understanding.md`.

### Gate 1

Check, in order:

- The `Task` call reported success.
- `jira-understanding.md` exists.
- Its H1 contains the requested Jira key.
- All eleven headings from the template are present: `## Summary`, `## Business Context`,
  `## Functional Requirements`, `## Acceptance Criteria`, `## Technical Requirements`,
  `## Important Jira Discussions`, `## Dependencies`, `## Edge Cases`,
  `## Testing Expectations`, `## Open Questions`, `## Assumptions and Inferences`.
- `## Summary`, `## Functional Requirements` and `## Acceptance Criteria` are non-empty. A
  section stating `None stated in Jira.` counts as filled — that is a real finding about the
  ticket, not a failure.

If Gate 1 fails, **STOP**. Do not run Agents 2, 3 or 4. Report which check failed and why. An
unread or misread ticket makes every downstream stage worthless.

## Step 3 — Agent 2, code understanding

One `Task` call, `subagent_type: understand-code-change-for-feature`. Pass the Jira key, the
absolute path to `jira-understanding.md`, and the absolute output path
`<artifacts>/feature-code-understanding.md`.

### Gate 2

Check, in order:

- The `Task` call reported success.
- `feature-code-understanding.md` exists.
- Its H1 contains the requested Jira key.
- Sections `## 1.` through `## 15.` are present, including the `## 3. Change-Set Resolution`
  sub-headings `### Repository State`, `### Resolution Rule`, `### Landing SHA`,
  `### Landing Type`, `### Diff Boundary`, `### Feature Commits`, `### Changed Files`,
  `### Confidence`, `### Ambiguities`.
- `### Landing SHA` names a concrete commit.
- `### Confidence` is `HIGH`, `MEDIUM` or `LOW` — not `UNRESOLVED`.
- No blocking ambiguity is recorded (`NO_MATCH_ON_SEARCH_REF`,
  `MULTIPLE_LANDING_CANDIDATES`, `LANDING_NEWER_THAN_CHECKOUT`). Advisory ambiguities
  (`INTERLEAVED_JIRA_KEYS`, `BRANCH_INTERNAL_MERGES`) pass the gate and are carried into the
  final report.

If Gate 2 fails, **STOP**. Do not run Agents 3 or 4 — their entire input is the implementation
boundary, and an uncertain boundary produces confident nonsense. Report the ambiguity code and
what would unblock it, in the subagent's words. Do not resolve the ambiguity yourself by
picking a commit.

If confidence is `LOW` but nothing blocking is recorded, continue and carry the `LOW`
confidence into the final report so the reader discounts the downstream analysis accordingly.

## Step 4 — Agents 3 and 4, in parallel

Emit **both `Task` calls in a single message**. That is what makes them run in parallel, and
their independence is a design requirement, not an optimisation: Agent 4 must not see Agent 3's
findings.

- `subagent_type: identify-bugs-introduced-by-code-change` — pass the Jira key, absolute paths
  to both upstream artifacts, and the output path `<artifacts>/bug-analysis.md`.
- `subagent_type: identify-tests-to-be-tested-by-qa-engineer` — pass the Jira key, absolute
  paths to both upstream artifacts, and the output path `<artifacts>/qa-test-scenarios.md`.
  State explicitly in the prompt that it must not read `bug-analysis.md`.

### Re-check the upstream artifacts first

Immediately before emitting the two `Task` calls, confirm that `jira-understanding.md` and
`feature-code-understanding.md` are still readable. Do not rely on Gates 1 and 2 having passed
earlier: `agent-artifacts/` is gitignored, so `git clean -fdx` removes it, and a workflow that
spans hours can lose its upstream artifacts between stages. Passing a path to an artifact that
no longer exists sends both agents into a degraded run for no reason.

If either is missing, re-run that stage before fanning out.

### Gate 3, independently per agent

Neither failure aborts the other; both have already received everything they need.

- **Agent 3** — `bug-analysis.md` exists, its H1 contains the key, and it has `## Findings`
  and `## Review Coverage`. `## Findings` containing exactly
  `No confirmed defects were identified in the reviewed change set.` is a pass. If Agent 3
  fails, record `Bug Analysis: FAILED` and still report Agent 4's result.
- **Agent 4** — `qa-test-scenarios.md` exists, its H1 contains the key, it has a four-column
  scenario table and a `## Delivery Status` block. Read the Jira update status from that block
  rather than assuming. If Agent 4 fails, record `QA Test Scenarios: FAILED` and
  `Jira QA Comment: FAILED`, and preserve every artifact produced so far.

## Step 5 — Final report

Report exactly this structure, with real values:

```text
UnderstandFeatureBasedOnJiraAndCode completed.

Jira: <JIRA-ID>

Agent 1 — Jira Understanding: SUCCESS
Artifact: <path>

Agent 2 — Code Understanding: SUCCESS
Artifact: <path>

Git Change Set:
Landing SHA: <sha>
Landing Type: <type>
Changed Files: <count>
Confidence: <level>
Ambiguities: <advisory codes, or none>

Agent 3 — Bug Analysis: SUCCESS / FAILED
Artifact: <path>
Findings: <n> High, <n> Medium, <n> Low

Agent 4 — QA Test Scenarios: SUCCESS / FAILED
Artifact: <path>
Scenarios: <count>

Jira QA Comment: SUCCESS / FAILED
<comment id, or the failure reason>

Overall Status: SUCCESS / PARTIAL / FAILED
```

Overall status:

- `SUCCESS` — all four agents passed their gates and the Jira comment was posted or updated.
- `PARTIAL` — Agents 1 and 2 passed but Agent 3 or Agent 4 failed, or the Jira comment failed
  while the scenarios artifact was written.
- `FAILED` — the workflow stopped at Gate 1 or Gate 2.

Then add two or three sentences of substance for a human: the most serious bug finding, the
number of QA scenarios and their acceptance-criteria coverage, and anything the reader should
distrust — `LOW` confidence, an advisory ambiguity, an off-checkout analysis, or a ticket too
thin to specify the feature. Never report a Jira update as successful when the delivery status
block says otherwise.

## Reference files

The subagents read these directly; you do not need to.

- `references/shared-rules.md` — accuracy and sourcing rules that bind every agent
- `references/artifact-contracts.md` — artifact paths, templates and who reads what
- `references/commit-resolution.md` — resolver usage, checkout modes, rules, ambiguity codes
- `references/bug-review-guide.md` — bug categories, method, priorities, finding format
- `references/qa-scenario-guide.md` — scenario design, table format, Jira comment delivery
- `references/omps-domain-checklist.md` — repository layering and OMPS regression traps
- `scripts/resolve_change_set.py` — the deterministic change-set resolver used by Agent 2
