# Bug review guide

The objective is to find defects **introduced or materially exposed by this change set** —
not to audit the repository. A pre-existing flaw that the change set neither touches nor
newly reaches is out of scope; say so once under `## Review Coverage` rather than reporting
it as a finding.

Review as if the author could have been anyone from a first-week joiner to a principal
engineer. Do not limit the review to syntax or style. Style, formatting and naming are not
defects.

## Method

For each candidate issue, work through all nine steps before writing anything down:

1. Identify the changed code.
2. Understand the surrounding execution path — read the callers and callees, not just the diff.
3. Determine the expected behaviour from Jira.
4. Determine the actual behaviour from the code.
5. Identify the mismatch precisely.
6. Determine whether the change set introduced it. If the same behaviour exists at the
   diff base, it is pre-existing.
7. Determine the production impact.
8. Determine reproducibility — can a QA engineer or an operator trigger it?
9. Assign a priority.

Verify step 6 against the diff base rather than assuming. `git show <diff-base>:<path>` and
`git diff --find-renames <base> <head> -- <path>` are the tools for this.

## Confirmed versus potential

- **Confirmed defect** — the code path is fully traced and the mismatch is visible in the
  source. You can point at the lines that do the wrong thing.
- **Potential defect** — the concern is real but resolving it needs runtime information,
  data-shape knowledge, configuration, or an external system's behaviour you cannot read.

Say which one, using those exact words, in the `Issue` field. Prefer three findings you can
defend over twelve you cannot. A speculative finding dressed up as confirmed destroys trust
in the whole report.

### The common hybrid

Most real findings are part confirmed and part unverifiable: the gap in the code is visible, but
its consequence depends on a system you cannot read. A missing validation is confirmed; what the
downstream service does with the unvalidated value is not.

Label these `Confirmed defect`, because the defect is the gap and the gap is in the source. Then
name the unverified link explicitly in `Impact` — "assuming IRS rejects an unknown model name,
which I could not verify here". Do not downgrade the whole finding to `Potential` because one
consequence is unconfirmed; that hides a real gap behind a hedge.

Reserve `Potential defect` for findings where the **gap itself** is uncertain — where the code
might be correct and you cannot tell.

## The four categories

Every finding is classified as exactly one of `Regression`, `Functional`, `Data Integrity`
or `Implementation Gap`. Use the lists below as review prompts — walk them deliberately
rather than skimming the diff and reporting what jumps out.

**When a finding fits several categories, classify by the cause, not the symptom.** Findings
routinely qualify under two or three lists — a missing bound is both "missing validation" (Data
Integrity) and "missing boundary check" (Implementation Gap), and if it newly exposes an existing
failure path it reads as Regression too. Ask what the author did or failed to do, not what goes
wrong downstream:

- The code does something incorrect with data it accepted → `Functional`.
- The code accepts, transforms or persists data it should not have, or its declared contract does
  not match what it produces → `Data Integrity`.
- Something the feature needed was simply never written → `Implementation Gap`.
- The change altered behaviour that already worked, or newly exposed a path that was previously
  unreachable → `Regression`.

Apply them in that order when two still fit, and say in `Issue` which other category it touches
rather than filing the same defect twice.

### Regression

Logic changes that alter existing API contracts, change behaviour consumers already depend
on, break shared utility functions, affect unrelated modules, break backward compatibility,
introduce side effects into existing flows, change a default unexpectedly, or break existing
callers. Pay attention to shared helpers: a signature or semantics change in a utility used
by sync, async and dry-run paths hits all three.

### Functional

Incorrect business logic, incorrect or missing conditions, wrong state transitions, invalid
assumptions, incomplete implementation of a requirement, wrong ordering of operations,
mishandled edge cases, unexpected behaviour on valid input, behaviour inconsistent with an
acceptance criterion. Ordering is a recurring source of real bugs: a value computed before
a step that can fail, and never reconciled afterwards, is a defect even though every
individual line looks right.

### Data Integrity

Null handling, missing validation, invalid parameter assumptions, incorrect request or
response schemas, serialization and deserialization problems, inconsistent data
transformations, missing required fields, invalid database assumptions, unhandled
asynchronous failures, partial failure handling, incorrect persistence. For generated APIs
check the schema itself: optional fields, absent `minimum` constraints and unexpressed
invariants are contract defects that force every client to defend itself.

### Implementation Gap

Incomplete handlers, missing error handling, missing error logging, hardcoded values,
missing boundary checks, missing timeout handling, missing retries where required, missing
cleanup, missing configuration, missing feature flag where one is required, dead code,
unreachable paths, incomplete integration behaviour. A requirement that is implemented at a
narrower scope than Jira asked for belongs here — for example a per-item summary where the
ticket asked for an aggregate.

## Priority

Use `High`, `Medium`, `Low`, reflecting realistic production impact and likelihood.

- **High** — major feature failure, widespread regression, significant production impact,
  data corruption, security exposure, severe outage.
- **Medium** — meaningful functional defect with limited scope or an available workaround.
- **Low** — minor behavioural or low-impact correctness issue.

Likelihood matters as much as severity. A data-corruption path that requires a
configuration nobody uses is not High.

Two cases that need a rule rather than a judgement call:

- **A pre-existing failure mode that the change makes newly triggerable.** Rate the *trigger*,
  not the underlying failure. Severity follows how reachable the change made it: a
  caller-controlled, unvalidated path into an existing failure is serious, while one needing
  privileged access or an unusual configuration is not. Say in `Issue` that the mechanism is
  pre-existing and only the reachability is new, so nobody reads it as newly written code.
- **A defect in an unreachable code path.** Cap it at `Low` and state the reachability plainly.
  Dead code is itself an `Implementation Gap`, so if the path should have been wired up and was
  not, *that* is the finding worth reporting and the flaw inside it is secondary.

## Finding format

Use exactly this structure for every finding. No alternative formats, no extra fields, no
omitted fields.

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

`Location` may list more than one path when a defect spans files; put the primary location
first. Cite it in the form `shared-rules.md` prescribes — prefer `File.java#methodName` over a
line number, and an anchor path such as `spec.yaml#components.parameters.Foo` for YAML. The
`<Line Number or Function Name>` wording in the template above allows either; the function or
anchor form is preferred because line numbers drift.

`Issue` opens with `Confirmed defect:` or `Potential defect:` and then explains the
flow — which method computes what, in which order, and where the mismatch appears.
`Steps to Reproduce` must be executable by someone with access to the service, not a
restatement of the code path.

Order findings High, then Medium, then Low.

## No findings

If nothing credible is found, the `## Findings` section contains exactly:

```markdown
No confirmed defects were identified in the reviewed change set.
```

Then still complete `## Review Coverage`, which is what makes the null result believable.
Never invent an issue to produce output.

## Review coverage

Close the artifact with a `## Review Coverage` section recording:

- **Changed-file review** — evidence that the whole change set was read rather than sampled.
  Give a row to every file that carries logic, including the ones where you found nothing.

  **Group the mechanical files instead of listing them individually.** On a large change set most
  files are one-line churn — `null` padding in mock stubs, a positional argument threaded through
  client overloads, generated sources, run configurations, formatting. A row each turns this
  section into a third of the artifact restating the word "mechanical". One row covering
  `17 test files padded with an extra positional argument — reviewed, no defect` carries the same
  evidentiary weight and stays readable. Name the group precisely enough that a reader can check
  it, and keep individual rows for anything with logic in it.
- **Test coverage assessment** — what the change set's tests do cover, and the specific
  gaps. Gaps are stated as the untested behaviour, not as "more tests needed".
- **Riskiest changes** — the two or three files where a mistake would have the widest blast
  radius, with the reason.
- **Regression assessment** — an explicit statement about which pre-existing behaviours were
  checked and found intact. "Additive change, no regression found in X, Y, Z" is a valuable
  conclusion when it is true and verified.
- **Verification limitations** — anything you could not check, stated plainly. If you did
  not run tests (this workflow does not), say the findings come from static analysis of the
  diff, the surrounding code and the existing tests.

## Depth benchmark

`docs/omps-5215-async-api-bug-review.md` is a hand-written review of a change set in this
repository and sets the standard for depth and tone. Note what it does: it traces the
ordering of summary calculation against downstream persistence to show that counts can
contradict the final outcome, it distinguishes an additive change from a regression and says
so explicitly, it reviews the OpenAPI schema as a contract rather than as configuration, it
reviews every changed file including the ones with no defect, it lists test gaps as concrete
untested scenarios, and it admits a verification limitation at the end instead of implying
more was checked than was.

Read it for depth and tone only — it predates this workflow and its **format is not the one to
copy**. Three specific divergences: it uses `P1`–`P3` priorities rather than `High`/`Medium`/`Low`;
it uses long prose category names such as "Functional bugs, incorrect logic, and unhandled edge
cases" rather than the four fixed categories; and its findings carry `**Affected files:**` and
`**Expected behavior:**` fields with no `Category:` or `Location:`. The format in this guide wins
on all three.

It also reviews three endpoints in one module. On a change set spanning many operations and
modules, do not scale its per-file structure up literally — group the mechanical files as
described above.
