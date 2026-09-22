# QA scenario guide

The deliverable is the set of scenarios a QA engineer must execute to validate this feature.
Scenarios come from the Jira requirements **and** the implementation as it was actually
written. Jira text alone produces scenarios that miss what the code really does; the code
alone produces scenarios that miss what the business asked for.

## Design process

For each requirement worth testing:

```text
Jira requirement → expected business behaviour → implementation path → risk / edge cases → QA scenario
```

Walking through the implementation path is what makes a scenario executable. It tells you
which endpoint to call, which headers the request needs, which table or stored procedure to
inspect afterwards, and which dependency to break to force the negative case.

## Quality rules

Every scenario answers five questions:

- What is being tested?
- What starting state is required?
- What actions does QA perform?
- What should happen?
- What special conditions or dependencies apply?

Too vague to ship:

```text
Test the API.
```

Correct level of detail:

```text
Verify that a request containing an invalid portfolio identifier is rejected with the
expected validation response and does not persist any changes.
```

A scenario is executable when a QA engineer who has not read the diff can run it. Name the
concrete endpoint and method, the concrete field or header, and the concrete observable
outcome — a status code, a response field value, a persisted row, a log entry, a queue
message. "Verify it behaves correctly" is not an expected output.

Where an exact value depends on the environment (a tenant id, a portfolio id, a file), say
what kind of value is needed rather than inventing one that looks real.

## Coverage checklist

Work through this list and include a scenario wherever the change set makes it relevant.
Skip the rest — padding the count with irrelevant scenarios makes the real ones easier to
skip.

Happy path; each acceptance criterion; each functional requirement; input validation;
boundary conditions; negative scenarios; error handling; null and empty values; invalid
parameters; state transitions; API contract shape and backward compatibility; authentication
and authorization; data persistence; data integrity; external integrations; asynchronous
behaviour; retry and failure handling; configuration and feature flags; regression of
behaviour that existed before the change; performance-sensitive behaviour; concurrency and
race conditions.

Where it makes a difference, split into separate scenarios for valid, invalid, missing and
boundary input, and for existing versus non-existing data, duplicate requests, partial
failures and dependency failures.

Three additions the generic list does not imply, each a place where this repository actually
breaks:

- **Parameter serialisation form.** For an array query parameter, comma-separated
  (`?models=a,b`) versus repeated (`?models=a&models=b`) is the likeliest interop break, and the
  spec's `style` and `explode` settings decide which the service accepts. Test the form the spec
  declares *and* the one it does not. Include the empty value, which is usually a different
  request from omitting the parameter altogether.
- **Batching and fan-out.** Where a request is split into batches or blocks before a downstream
  call, a pass-through value can reach the first batch and be dropped from the rest. Use enough
  data to force more than one batch rather than testing only the single-batch path.
- **Lazy streaming responses.** Endpoints typed `Stream<T>` do their downstream work during
  response serialisation, after HTTP 200 and the headers are committed, so a failure truncates
  the body instead of returning an error status. Test the failure case on streaming endpoints
  specifically and assert on body completeness, not on the status code. This is not what
  "asynchronous behaviour" means in the list above, which in this codebase reads as the RabbitMQ
  import path; see the streaming notes in `omps-domain-checklist.md`.

Backward compatibility deserves particular attention on an additive change: an existing
client that does not know about the new field must keep working, and data written before the
change must still read correctly.

## Traceability

Each scenario's `Notes` carry the traceability, with no extra table columns: the acceptance
criteria (`AC-1`, `AC-2`, … as stated in Jira, or `AC-D1`, `AC-D2`, … where Agent 1 derived them),
the functional requirements (`FR-1`, `FR-2`, …), implementation paths and edge cases it covers.

**Never cite an identifier whose text you have not read.** If `jira-understanding.md` is missing,
those identifiers are unavailable, and mapping scenarios onto `FR-3` or `AC-D2` without knowing
what they say is fabrication even when the numbers happen to exist. Fall back to quoting the
requirement from its source — the Jira description bullet or the acceptance criterion itself —
under your own clearly-labelled scheme, and record in `## Coverage Notes` that a re-run with the
artifact present should re-map onto Stage 1's identifiers.

```text
Notes: Covers AC-3 and the null-input validation path in InstrumentValidatorServiceImpl.
```

Aim to cover every `AC-n`. If an acceptance criterion cannot be tested by QA — because it is
internal, or unobservable from outside — say so in the artifact rather than writing a
scenario that cannot be run.

## Table format

Exactly four columns, in this order:

```markdown
| TestScenario | Steps | Expected Output | Notes |
|---|---|---|---|
```

Cells must stay on one line. Jira converts markdown to ADF, and a newline inside a cell breaks
the table. Number the steps inline instead — but **never start a cell with a bare `1.`**. The ADF
converter reads a leading `1.` as the start of an ordered list and consumes the marker, so the
cell arrives in Jira reading `Pick a tenant … 2. Send …` with the first step's number silently
missing. Prefix the first step so the parser does not see a list:

```text
Step 1: call POST /v3/portfolios with a factorModels array containing two ids. 2. Wait for the 200 response. 3. Inspect the resolutionInfo of each returned position.
```

Other conversion quirks, all observed in this Jira instance:

- **Pipes** end the cell. Never put one inside a cell; write alternatives in words.
- **Asterisks** get escaped, so `*-test-functional` arrives as `\*-test-functional`. Name such
  modules in prose — "the functional test modules" — rather than with a glob.
- **Anchor paths containing `#`, `{` or `}`** render unreliably. Describe the location in prose
  for the Jira comment and keep the precise anchor in the artifact.
- The header separator `|---|` may be rewritten as `| --- |`. Harmless.

Keep each cell readable. A scenario needing more than roughly eight steps is probably two
scenarios — but a single scenario that runs the *same* check against several endpoints is one row,
not one row per endpoint. Say "against each of the four position endpoints listed in Notes" rather
than generating near-duplicate rows; a table of forty rows that differ only by URL is harder to
execute, not more thorough.

## Jira delivery

Scenarios are delivered as a **comment** on the issue. The description is never edited —
`editJiraIssue` is not used by this workflow. A comment is safe to re-run, attributable and
does not risk damaging requirement text that other people own.

The comment body starts with a fixed marker so repeat runs update instead of duplicating:

```markdown
## QA Test Scenarios

_Generated by UnderstandFeatureBasedOnJiraAndCode for <JIRA-ID> — change set <short-sha>_

| TestScenario | Steps | Expected Output | Notes |
|---|---|---|---|
| ... | ... | ... | ... |
```

Idempotency procedure:

1. `getJiraIssue(cloudId, issueIdOrKey=<KEY>, fields=["comment"], responseContentFormat="markdown")`.
2. Find a comment whose body contains the `## QA Test Scenarios` marker line.
3. If one exists, call `addCommentToJiraIssue` with that comment's `commentId` to update it
   in place.
4. Otherwise call `addCommentToJiraIssue` without `commentId` to add a new comment.

Use `contentFormat: "markdown"`. Running the workflow twice must leave exactly one QA
Test Scenarios comment.

## Honest reporting

If scenario generation succeeds but the Jira call fails, keep `qa-test-scenarios.md`, record
`Jira Update Status: Failed` with the error, and do not claim Jira was updated. A preserved
artifact plus an honest failure is a usable outcome; a false success is not.
