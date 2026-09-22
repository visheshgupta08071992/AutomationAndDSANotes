# Complete Agentic Workflow: Jira → Code → Bug Analysis → QA Test Scenarios

## 1. Objective

Create a reusable orchestration skill named:

`UnderstandFeatureBasedOnJiraAndCode`

The skill must provide an end-to-end understanding and validation workflow for a Jira feature.

The workflow consists of:

1. Understanding the Jira requirement.
2. Understanding the exact code changes implementing the feature.
3. Critically reviewing the implementation for bugs and risks.
4. Identifying comprehensive QA test scenarios.
5. Updating the Jira description with the generated QA test scenarios.

The architecture must separate **orchestration** from **specialized reasoning**.

The orchestration skill coordinates the workflow.

Specialized agents perform the actual analysis.

---

# 2. High-Level Architecture

```text
                UnderstandFeatureBasedOnJiraAndCode
                              │
                              ▼
              ┌───────────────────────────────┐
              │ UnderstandFeatureBasedOnJira  │
              │ Agent                         │
              └───────────────┬───────────────┘
                              │
                              ▼
                   jira-understanding.md
                              │
                              ▼
              ┌───────────────────────────────┐
              │ UnderstandCodeChangeForFeature│
              │ Agent                         │
              └───────────────┬───────────────┘
                              │
                              ▼
                feature-code-understanding.md
                              │
                   ┌──────────┴──────────┐
                   │                     │
                   ▼                     ▼
       ┌──────────────────────┐  ┌────────────────────────┐
       │ IdentifyAllBugs      │  │ IdentifyTestToBeTested │
       │ IntroducedByCodeChange│ │ ByQAEngineer           │
       │ Agent                │  │ Agent                  │
       └───────────┬──────────┘  └────────────┬───────────┘
                   │                          │
                   ▼                          ▼
              Bug Report              Jira Test Scenarios
```

Agents 3 and 4 MUST NOT depend on each other.

Both consume the evidence produced by Agents 1 and 2.

---

# 3. Components

## Skill

`UnderstandFeatureBasedOnJiraAndCode`

Responsibility:

- Accept input.
- Validate input.
- Execute agents in the correct order.
- Manage artifact handoffs.
- Validate intermediate outputs.
- Trigger downstream analysis.
- Handle failures safely.
- Return the final workflow status.

The skill itself should NOT perform detailed Jira analysis, Git analysis, bug analysis, or test design.

---

## Agent 1

`UnderstandFeatureBasedOnJira`

Responsibility:

Understand the Jira requirement and produce:

`jira-understanding.md`

---

## Agent 2

`UnderstandCodeChangeForFeature`

Responsibility:

Understand the exact implementation and produce:

`feature-code-understanding.md`

---

## Agent 3

`IdentifyAllBugsIntroducedByCodeChange`

Responsibility:

Critically review the implementation and identify defects introduced by the feature change.

Primary inputs:

- `jira-understanding.md`
- `feature-code-understanding.md`

The agent must focus on defects introduced or caused by the identified change set.

---

## Agent 4

`IdentifyTestToBeTestedByQAEngineer`

Responsibility:

Derive comprehensive QA test scenarios from:

- Jira requirements
- Acceptance criteria
- Actual implementation
- Identified workflows
- Relevant edge cases
- Existing tests
- Integration behavior

The agent must write the resulting test scenarios into the Jira description using the Atlassian connector.

---

# 4. Input Contract

The skill accepts:

```text
jiraId: string
```

Example:

```text
XYZ-123
```

The same `jiraId` must be passed consistently to all agents.

---

# 5. Orchestration Workflow

The execution order must be:

```text
START
  │
  ▼
Validate Jira ID
  │
  ▼
Agent 1: UnderstandFeatureBasedOnJira
  │
  ▼
Validate Jira Artifact
  │
  ▼
Agent 2: UnderstandCodeChangeForFeature
  │
  ▼
Validate Code Understanding Artifact
  │
  ├──────────────────────────────┐
  ▼                              ▼
Agent 3                       Agent 4
Bug Analysis                  QA Test Analysis
  │                              │
  ▼                              ▼
Bug Report                    Jira Update
  │                              │
  └──────────────┬───────────────┘
                 ▼
          Workflow Completion
```

Agents 3 and 4 may execute in parallel once Agents 1 and 2 have successfully completed.

---

# 6. Stage 1 — UnderstandFeatureBasedOnJira

Invoke:

```text
UnderstandFeatureBasedOnJira(
    jiraId = <jiraId>
)
```

The agent must retrieve and understand the Jira issue using the available Atlassian/Jira connector.

It should analyze, where available:

- Summary
- Description
- Business context
- Functional requirements
- Technical requirements
- Acceptance criteria
- Jira comments
- Decisions
- Clarifications
- Linked issues
- Dependencies
- Referenced documentation
- Attachments
- Edge cases
- Testing expectations

The agent must distinguish:

- Explicit Jira requirements
- Inferences
- Assumptions
- Open questions

It must never represent an inference as an explicit requirement.

---

# 7. Jira Understanding Artifact

Agent 1 must create:

```text
<agent-artifacts>/<jiraId>/jira-understanding.md
```

Minimum structure:

```markdown
# Jira Understanding - <JIRA_ID>

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

---

# 8. Stage 1 Validation

The orchestration skill must verify:

- Agent 1 succeeded.
- The artifact exists.
- The artifact corresponds to the requested Jira ID.
- The artifact contains meaningful Jira understanding.

If Agent 1 fails:

```text
STOP
```

Do not invoke Agent 2, Agent 3, or Agent 4.

---

# 9. Stage 2 — UnderstandCodeChangeForFeature

Invoke:

```text
UnderstandCodeChangeForFeature(
    jiraId = <jiraId>,
    jiraUnderstandingArtifact =
        <agent-artifacts>/<jiraId>/jira-understanding.md
)
```

The agent must first consume the Jira understanding.

It must use the local Git repository available in the IDE/workspace as the authoritative source for identifying code changes.

---

# 10. Repository and Git Analysis

The agent must determine:

- Current branch
- Base branch
- Whether the feature is currently on a feature branch
- Whether the feature has already been merged into `master`

## Feature branch

When operating on a feature branch:

- Identify the appropriate base/merge-base.
- Identify commits belonging to the feature.
- Identify changed files.
- Analyze added, deleted, and renamed files.
- Analyze relevant tests and configuration.
- Establish the precise feature boundary.

## Master branch

When operating on `master`, use the following mandatory resolution rules.

### Rule 1 — First-parent search

```bash
git log --first-parent --oneline --grep=<JIRA_ID> master
```

Do not treat:

```bash
git log --grep=<JIRA_ID> master
```

as an equivalent feature-resolution strategy.

First-parent history must be the primary landing-point search.

### Rule 2 — Loose commit tracing

If the Jira key does not identify the landing:

```bash
git log --no-merges --oneline --grep=<JIRA_ID> master
```

Then trace candidate commits:

```bash
git rev-list --ancestry-path --merges <sha>..master | tail -1
```

Before trusting the result:

```bash
git rev-list --first-parent master | grep -q <sha> \
  && echo ON_CHAIN \
  || echo VIA_MERGE
```

### Rule 3 — Determine commit shape

```bash
git rev-list --parents -n 1 <sha>
```

For a merge:

```bash
git diff --find-renames M^1 M
```

For squash/direct commits:

```bash
git show --find-renames C
```

For rebased commit series, analyze the relevant individual commit patches.

### Rule 4 — Verify the boundary

For a merge:

```bash
git diff --stat --find-renames M^1 M
```

Also inspect branch-internal merges:

```bash
git rev-list --merges M^1..M^2
```

Potentially unrelated/interleaved changes must be explicitly identified.

### Rule 5 — Fallbacks

Use, in order:

```bash
git log --first-parent --oneline --grep='Merged PR <PR_NUMBER>' master
```

and:

```bash
git log -S"<identifier>" \
  --first-parent \
  --oneline \
  master \
  -- "<appropriate-path>"
```

Date/author searches are candidates only.

Never treat them as an exact feature resolution.

---

# 11. Change-Set Resolution Guard

Before deep code analysis, the agent must establish:

```text
Jira ID:
Current branch:
Base branch:

Resolution rule:
Landing SHA:
Landing type:

Diff base:
Diff head:

Feature commit count:
Changed file count:

Confidence:
Ambiguities:
```

If the feature change set cannot be determined unambiguously:

```text
STOP
```

Do not guess.

Do not proceed to bug analysis or QA analysis using an uncertain implementation boundary.

---

# 12. Code Understanding

Once the change set is established:

- Analyze the changed files.
- Explore the relevant surrounding code.
- Trace actual execution paths.
- Understand existing behavior affected by the change.
- Identify APIs and contracts.
- Understand services and business logic.
- Analyze persistence.
- Analyze external integrations.
- Analyze configuration and feature flags.
- Analyze error handling.
- Analyze authorization/security behavior.
- Analyze events/messages.
- Analyze tests.

The diff establishes:

```text
WHAT changed
```

The broader codebase analysis establishes:

```text
HOW the feature works
```

Do not restrict the analysis to files directly changed by the feature when surrounding code is required to understand behavior.

---

# 13. Jira-to-Code Mapping

For each significant requirement:

```text
Requirement
    ↓
Implementation
    ↓
Class / Method
    ↓
Test
```

Identify:

- Implemented requirements
- Partially implemented requirements
- Requirements implemented differently from Jira
- Requirements not found

Do not classify something as missing without inspecting relevant pre-existing behavior.

---

# 14. Code Understanding Artifact

Agent 2 must create:

```text
<agent-artifacts>/<jiraId>/feature-code-understanding.md
```

Minimum structure:

```markdown
# Feature Understanding - <JIRA_ID>

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

---

# 15. Stage 2 Validation

The orchestration skill must verify:

- Agent 2 succeeded.
- The feature understanding artifact exists.
- The artifact corresponds to the correct Jira ID.
- The Git change set was resolved.
- No unresolved change-set ambiguity exists.

Only after this validation may Agents 3 and 4 execute.

---

# 16. Agent 3 — IdentifyAllBugsIntroducedByCodeChange

## Objective

Critically review the implementation described in:

```text
jira-understanding.md
feature-code-understanding.md
```

The objective is to identify defects introduced by the feature's code changes.

The review must account for varying levels of developer experience.

Do not limit the review to obvious syntax or coding mistakes.

Review:

- Business logic
- Control flow
- State transitions
- Existing behavior
- API contracts
- Data contracts
- Error handling
- Nullability
- Validation
- Concurrency/asynchronous behavior
- Integration behavior
- Operational behavior
- Boundary conditions
- Regression risk

---

# 17. Bug Categories

Evaluate every relevant area against these four categories.

## 17.1 Regression Risks

Identify logic changes that may:

- Alter existing API contracts.
- Change behavior expected by consumers.
- Break shared utility functions.
- Affect unrelated modules.
- Change backward compatibility.
- Introduce side effects into existing flows.
- Change default behavior unexpectedly.
- Break existing callers.

---

## 17.2 Functional & Logical Defects

Identify:

- Incorrect business logic.
- Incorrect conditions.
- Missing conditions.
- Incorrect state transitions.
- Invalid assumptions.
- Incomplete implementation of requirements.
- Incorrect ordering of operations.
- Incorrect handling of edge cases.
- Unexpected behavior under valid inputs.
- Behavior inconsistent with acceptance criteria.

---

## 17.3 Data & Contract Integrity

Check for:

- `null` / `undefined` handling problems.
- Missing validation.
- Invalid parameter assumptions.
- Incorrect request/response schemas.
- Incorrect serialization/deserialization.
- Inconsistent data transformations.
- Missing required fields.
- Invalid database assumptions.
- Unhandled asynchronous failures.
- Partial failure handling.
- Incorrect data persistence.

---

## 17.4 Implementation Gaps

Check for:

- Incomplete handlers.
- Missing error handling.
- Missing error logging.
- Hardcoded values.
- Missing boundary checks.
- Missing timeout handling.
- Missing retries where required.
- Missing cleanup.
- Missing configuration.
- Missing feature flags where required.
- Dead code.
- Unreachable paths.
- Incomplete integration behavior.

---

# 18. Bug-Review Methodology

For each potential issue:

1. Identify the changed code.
2. Understand the surrounding execution path.
3. Determine the expected behavior from Jira.
4. Determine the actual behavior from the code.
5. Identify the mismatch.
6. Determine whether the defect was introduced by the feature change.
7. Determine production impact.
8. Determine reproducibility.
9. Assign an appropriate priority.

Do not report speculative concerns as confirmed bugs.

Use wording such as:

- "Confirmed defect" when evidence is strong.
- "Potential defect" when additional runtime/context information is required.

Prefer fewer high-confidence findings over many speculative findings.

---

# 19. Bug Priority

Use:

```text
High
Medium
Low
```

Priority must reflect realistic production impact and likelihood.

Examples:

- `High` — major feature failure, widespread regression, significant production impact,data corruption, security exposure, severe system outage.
- `Medium` — meaningful functional defect with limited scope/workaround.
- `Low` — minor behavior or low-impact correctness issue.

---

# 20. Bug Output Format

The evaluation output MUST use exactly this structure for each finding:

```markdown
### [Priority] — <Short Description>
- **Category:** <Regression | Functional | Data Integrity | Implementation Gap>
- **Location:** `<File Path>:<Line Number or Function Name>`
- **Issue:** <Detailed explanation of the flaw based on code flow>
- **Impact:** <Production consequence if unaddressed>
- **Steps to Reproduce:**
  1. <Step 1>
  2. <Step 2>
```

Do not add alternative formats.

Do not create findings without sufficient evidence.

---

# 21. Agent 3 Output Artifact

Create:

```text
<agent-artifacts>/<jiraId>/bug-analysis.md
```

The artifact should contain only the bug findings in the required format.

If no credible defects are identified, state:

```markdown
No confirmed defects were identified in the reviewed change set.
```

Do not invent issues simply to produce output.

---

# 22. Agent 4 — IdentifyTestToBeTestedByQAEngineer

## Objective

Identify the complete set of QA test scenarios required to validate the Jira feature.

The agent must consume:

```text
jira-understanding.md
feature-code-understanding.md
```

The agent must not generate tests solely from Jira text.

The actual implementation and runtime workflow must also influence the test scenarios.

---

# 23. QA Analysis Scope

Identify tests for:

- Happy-path behavior.
- Acceptance criteria.
- Functional requirements.
- Input validation.
- Boundary conditions.
- Negative scenarios.
- Error handling.
- Null/empty values.
- Invalid parameters.
- State transitions.
- API contracts.
- Authentication/authorization where applicable.
- Data persistence.
- Data integrity.
- External integrations.
- Asynchronous behavior.
- Retry/failure scenarios.
- Configuration/feature flags.
- Regression behavior.
- Backward compatibility.
- Performance-sensitive behavior where relevant.
- Concurrency/race conditions where relevant.

Do not generate irrelevant tests simply to increase the test count.

---

# 24. QA Test Design Process

For each important requirement:

```text
Jira Requirement
       ↓
Expected Business Behavior
       ↓
Implementation Path
       ↓
Risk / Edge Cases
       ↓
QA Test Scenario
```

Test scenarios must be specific enough that a QA engineer can execute them without independently reconstructing the implementation.

---

# 25. Test Scenario Quality Rules

Each scenario must answer:

- What is being tested?
- What starting state is required?
- What actions should QA perform?
- What should happen?
- What special conditions or dependencies exist?

Avoid vague scenarios such as:

```text
Test the API.
```

Prefer:

```text
Verify that a request containing an invalid portfolio identifier
is rejected with the expected validation response and does not
persist any changes.
```

Where appropriate, include separate scenarios for:

- Valid input
- Invalid input
- Missing input
- Boundary input
- Existing data
- Non-existing data
- Duplicate requests
- Partial failures
- Dependency failures

---

# 26. Jira Description Update

Agent 4 must update the Jira issue description using the Atlassian connector.

The test scenarios must be added in a clearly identifiable section:

```markdown
## QA Test Scenarios
```

The scenarios must be represented as a Markdown table with exactly these columns:

| TestScenario | Steps | Expected Output | Notes |
|---|---|---|---|
| ... | ... | ... | ... |

---

# 27. Jira Update Rules

When updating the Jira description:

1. Retrieve the current Jira description first.
2. Preserve existing Jira content.
3. Do not overwrite unrelated sections.
4. Add or update the `## QA Test Scenarios` section.
5. If the section already exists, replace/update that section rather than creating a duplicate.
6. Preserve all existing information outside that section.
7. Keep the table valid Markdown.
8. Ensure scenarios are readable by a QA engineer.
9. Do not add speculative or irrelevant scenarios.
10. Do not remove existing Jira content unrelated to QA scenarios.

The operation must be idempotent.

Running the agent twice should not create duplicate QA sections or duplicate scenarios.

---

# 28. QA Agent Output Artifact

After successfully updating Jira, create:

```text
<agent-artifacts>/<jiraId>/qa-test-scenarios.md
```

The artifact should contain:

```markdown
# QA Test Scenarios - <JIRA_ID>

| TestScenario | Steps | Expected Output | Notes |
|---|---|---|---|
| ... | ... | ... | ... |
```

Also include:

```text
Jira Update Status:
Updated / Failed

Jira Issue:
<JIRA_ID>

Section Updated:
QA Test Scenarios
```

---

# 29. QA Traceability

Where practical, each scenario should be traceable to one or more:

- Jira acceptance criteria.
- Functional requirements.
- Implementation paths.
- Identified risks.
- Edge cases.

The traceability may be captured in `Notes` without adding additional Jira table columns.

Example:

```text
Notes:
Covers acceptance criterion AC-3 and the null-input validation path.
```

---

# 30. Failure Handling

## Agent 1 Failure

Stop the workflow.

Do not execute downstream agents.

---

## Agent 2 Failure

Stop the workflow.

Do not run Agents 3 or 4 because their implementation context is incomplete.

---

## Agent 3 Failure

Do not fail the entire workflow if Agent 4 can safely run.

Record:

```text
Bug Analysis: FAILED
```

and continue with Agent 4.

---

## Agent 4 Failure

Do not discard the outputs of Agents 1–3.

Record:

```text
QA Test Scenario Generation: FAILED
Jira Update: FAILED
```

Preserve all artifacts already generated.

---

## Jira Update Failure

If the QA agent successfully generates scenarios but cannot update Jira:

- Preserve `qa-test-scenarios.md`.
- Report the Jira update failure.
- Do not claim that Jira was updated.

---

# 31. Final Workflow Summary

The orchestration skill should return:

```text
UnderstandFeatureBasedOnJiraAndCode completed.

Jira: <JIRA_ID>

Agent 1 — Jira Understanding:
SUCCESS
Artifact:
<path>

Agent 2 — Code Understanding:
SUCCESS
Artifact:
<path>

Git Change Set:
Landing SHA: <SHA>
Landing Type: <Type>
Changed Files: <Count>
Confidence: <Level>

Agent 3 — Bug Analysis:
SUCCESS / FAILED
Artifact:
<path>

Confirmed Bugs:
<Count>

Agent 4 — QA Test Scenarios:
SUCCESS / FAILED
Artifact:
<path>

Jira Test Scenario Update:
SUCCESS / FAILED

Overall Status:
SUCCESS / PARTIAL / FAILED
```

---

# 32. Global Accuracy Rules

These rules apply to all agents.

1. Never guess.
2. Never fabricate Jira requirements.
3. Never fabricate Git history.
4. Never fabricate code behavior.
5. Never fabricate review comments.
6. Never fabricate bugs.
7. Never fabricate test results.
8. Clearly distinguish facts from assumptions.
9. Clearly distinguish confirmed defects from potential concerns.
10. Do not treat ambiguous Git history as a resolved change set.
11. Preserve evidence and artifacts between agent stages.
12. Use Jira as the source of truth for stated requirements.
13. Use the local Git repository as the source of truth for feature change history.
14. Use the actual codebase as the source of truth for implementation behavior.
15. Use the identified implementation to derive realistic QA scenarios.
16. Do not allow one incorrect assumption to propagate silently through downstream agents.
17. When evidence is insufficient, explicitly state that it is insufficient.
18. Prefer stopping or reporting uncertainty over producing a confident but incorrect result.

---

# 33. Shared Artifact Contract

All agents must use the following artifact structure:

```text
<agent-artifacts>/
└── <jiraId>/
    ├── jira-understanding.md
    ├── feature-code-understanding.md
    ├── bug-analysis.md
    └── qa-test-scenarios.md
```

This directory acts as the persistent shared context for the workflow.

---

# 34. Definition of Done

The workflow is considered complete when:

```text
                         Jira Feature
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Jira Understanding  │
                  │ Agent 1              │
                  └──────────┬──────────┘
                             │
                             ▼
                    jira-understanding.md
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Code Understanding  │
                  │ Agent 2              │
                  └──────────┬──────────┘
                             │
                             ▼
                feature-code-understanding.md
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
             ┌────────────┐    ┌────────────┐
             │ Bug Agent  │    │ QA Agent   │
             │ Agent 3    │    │ Agent 4    │
             └─────┬──────┘    └─────┬──────┘
                   │                  │
                   ▼                  ▼
             bug-analysis.md    Jira updated
                                      │
                                      ▼
                            qa-test-scenarios.md
```

The workflow should provide four distinct outcomes:

### Functional Understanding

What the feature is supposed to do.

### Technical Understanding

How the feature was implemented.

### Risk Understanding

What bugs or regressions may exist in the implementation.

### QA Understanding

What QA should test to validate the feature comprehensively.

The combined workflow should enable a developer, reviewer, or QA engineer to understand the feature without independently reconstructing the Jira ticket, Git history, implementation, defects, and test strategy.