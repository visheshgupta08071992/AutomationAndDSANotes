# Artifact contracts

The shared context for one workflow run lives in a single directory at the repository root:

```text
agent-artifacts/
└── <JIRA-ID>/
    ├── jira-understanding.md          (Agent 1)
    ├── feature-code-understanding.md  (Agent 2)
    ├── bug-analysis.md                (Agent 3)
    └── qa-test-scenarios.md           (Agent 4)
```

`agent-artifacts/` is gitignored. Nothing here is meant to be committed.

Two consequences worth knowing before you rely on a path here. `git clean -fdx` deletes the whole
directory along with other ignored files, so artifacts do not survive a working-tree clean — a
workflow spanning hours can lose an earlier stage's output. And file-search tools respect ignore
rules, so these paths will not appear in glob or search results even when the files exist; read
them directly by path. Never conclude an artifact is missing because a search did not list it,
and never assume it is present because an earlier stage reported success.

Each agent owns exactly one file and treats the others as read-only. The orchestrator
passes absolute paths, so no agent needs to guess where anything lives.

## Who reads what

| Agent | Reads | Writes |
|---|---|---|
| 1 — jira understanding | Jira | `jira-understanding.md` |
| 2 — code understanding | `jira-understanding.md`, git, code | `feature-code-understanding.md` |
| 3 — bug analysis | both upstream artifacts, code | `bug-analysis.md` |
| 4 — QA scenarios | both upstream artifacts, code, tests | `qa-test-scenarios.md` + one Jira comment |

Agent 4 must **not** read `bug-analysis.md`. Agents 3 and 4 run in parallel and must reach
their conclusions independently; a QA scenario set that is derived from the bug report is
just a restatement of Agent 3's opinion and loses its value as a cross-check.

## Templates

### `jira-understanding.md` (Agent 1)

```markdown
# Jira Understanding - <JIRA-ID>

## Summary
## Business Context
## Functional Requirements
## Acceptance Criteria
## Technical Requirements
## Important Jira Discussions
## Dependencies
## Edge Cases
## Testing Expectations
## Open Questions
## Assumptions and Inferences
```

### `feature-code-understanding.md` (Agent 2)

```markdown
# Feature Understanding - <JIRA-ID>

## 1. Executive Summary
## 2. Jira Requirement Summary
## 3. Change-Set Resolution
### Repository State
### Resolution Rule
### Landing SHA
### Landing Type
### Diff Boundary
### Feature Commits
### Changed Files
### Confidence
### Ambiguities
## 4. Architecture Overview
## 5. End-to-End Feature Workflow
## 6. Detailed Implementation
## 7. Classes and Files Impacted
## 8. Jira Requirement → Code Mapping
## 9. Important Methods and Logic
## 10. Review Comments and Decisions
## 11. Tests and Coverage
## 12. Edge Cases
## 13. Risks and Important Observations
## 14. Open Questions
## 15. Summary for Future Developers
```

### `bug-analysis.md` (Agent 3)

```markdown
# Bug Analysis - <JIRA-ID>

_Change set: <landing-short-sha> (<landing-type>), <n> files changed_

## Findings

### [High] — <short description>
...

## Review Coverage
```

Findings use the exact format in `bug-review-guide.md`, ordered High, then Medium, then Low.

### `qa-test-scenarios.md` (Agent 4)

```markdown
# QA Test Scenarios - <JIRA-ID>

_Change set: <landing-short-sha>_

| TestScenario | Steps | Expected Output | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

## Coverage Notes

## Delivery Status

Jira Update Status: Updated (comment <id>) / Failed
Jira Issue: <JIRA-ID>
Delivery: Jira comment
Section: QA Test Scenarios
```

## Stage gates

The orchestrator validates each artifact before the next stage starts. An artifact passes
only when the file exists, its H1 contains the requested Jira key, every prescribed
heading is present, and no required section is empty. Stage 2 additionally requires a
Landing SHA and a confidence that is not `UNRESOLVED`.

Write the headings exactly as templated. A renamed or dropped heading fails the gate and
stops the workflow even when the analysis itself is sound.
