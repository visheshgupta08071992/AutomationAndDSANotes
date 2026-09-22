# OMPS domain checklist

Repository-specific knowledge for tracing implementations and spotting regressions in
`portfolio-services`. `AGENTS.md` at the repo root is the fuller description; this file is
the part that changes how you analyse a change set.

## Trace the real layering

A change to a portfolio endpoint is almost never confined to the files in the diff. Follow
the chain:

```text
api-schema/*.yaml  →  generated *-api-v* interface  →  Controller  →  *ServiceAdaptorV3
  →  *Service / *ServiceImpl  →  *Dao (JdbcTemplate → SQL Server stored procedure)
```

- **Generated API modules** (`portfolio-api-v3`, `portfolio-integration-api-v1`,
  `portfolio-experience-api-v1`, `portfolio-metrics-api-v1`, `portfolio-admin-api-v2`) are
  generated at build time from `api-schema/*.yaml` by `api-gen.gradle`. The YAML is the
  contract. A field added to the spec changes every generated client, so read spec diffs as
  public API changes.
- **Adaptors** (`*ServiceAdaptorV3`, `*ServiceAdaptorV1`) translate API models to domain
  models, one per API version. A domain-model change with only one adaptor updated is a
  classic partial implementation — check every adaptor that touches the changed model.
- **DAOs** call stored procedures (`{call ps.LoadStagedPositions(...)}`,
  `ps.GetPortfolioSnapshot`, …) through `JdbcTemplate`. There is no ORM. Parameter order and
  count matter, and the proc source is in the repo.
- **Liquibase** owns the schema. Tenant changelogs live under
  `portfolio-service/src/main/resources/db/changelog/**`, catalog changelogs under
  `db/catalog_changelog/**`, with procedure sources in `procs` subfolders.
- **Shared code** is in `portfolio-service-libs/` as paired `lib-X` / `starter-X` modules.
  Services depend on the starter, never the lib.
- **Package roots are inconsistent** for historical reasons: older code is
  `com.msci.cdms2.portfolio.*`, newer shared libs are `com.msci.omps.*`, experience and
  import code is `com.msci.portfolio.*`. Search all three before concluding something does
  not exist.

### Generator configuration is behaviour, not build plumbing

This is the blind spot a diff will not reveal, because the decisive file is often neither
changed, nor Java, nor a caller or callee of anything in the change set.

When a change adds or alters a field on a generated model or a generated request, read the
per-module `java-spring-config.yaml` and the shared mustache overrides in `api-templates/`
before describing the runtime behaviour. They determine things you cannot infer from the Java:

- Whether a null field is **omitted from the serialised request body or sent as an explicit
  `null`** — a difference the receiving service usually treats as two different requests.
- Whether `sortParamsByRequiredFlag` is set, which decides whether **spec parameter order is
  method signature order**. When it is `false`, inserting a parameter in the middle of a spec
  silently reorders a generated method's arguments.
- How optional and nullable map onto the generated types.

The same applies in reverse: a change to a `java-spring-config.yaml` or a mustache template is
a behaviour change across every operation the module generates, even with no Java in the diff.

## Cross-cutting behaviour to check on every change

### Multi-tenancy

Every request resolves an OMPS Schema (historically "client ID" / "tenant ID"). `TenantFilter`
in `lib-tenants` reads the authenticated principal, resolves the profile through OMES when
`MSCI-PROFILE-ID` is present, and otherwise falls back to `SECURITY-TENANT-ID`
(`X-MSCI-Client-ID` is a deprecated synonym and `SECURITY-TENANT-ID` wins). The result is the
thread-bound `TenantContext`, which also carries the system-schema override, ACL
super/restricted-read flags and shadow-write / insert-only modes. `lib-dbcore` resolves the
tenant in the catalog database, pulls credentials from Azure Key Vault and routes to the
per-tenant datasource.

What this means for review:

- Anything that runs outside an HTTP request — a scheduled job, a worker consuming from
  RabbitMQ, a new thread, a parallel stream, an async or `CompletableFuture` continuation —
  must set `TenantContext` explicitly. `TenantContext` is thread-bound, so work handed to
  another thread loses it. This is the single most common source of high-severity defects in
  this repo.
- Connection and credential failures surface as `DatabaseNotFoundException` and
  `DatabaseCredentialsNotFoundInKeyVaultException`, not as generic SQL errors.
- ACL flags (super read, restricted read) change what a query returns. A new read path must
  honour them the way the existing paths do.

### Bi-temporality

`asOfDate` (business/valid time, a path parameter) and `asAt` (system/transaction time, an
optional query parameter backed by SQL Server temporal tables) are orthogonal. Positions live
in `ps.PortfolioSnapshotPosition` (non-temporal, bulk writes) and
`ps.PortfolioSnapshotPositionOverride` (temporal, with `isDeleted` for logical deletes), and
reads UNION the two. Deletes are logical; only the purging job removes rows.

What this means for review:

- A new or modified read path that touches only one of the two tables returns wrong data.
- Logical deletes must be respected — a read that ignores `isDeleted` resurrects deleted
  positions.
- A change that handles `asOfDate` but drops or ignores `asAt` silently breaks point-in-time
  queries.

### Auth, enrichment, async, filtering

- **Auth**: MSCI solutions-auth (Auth0 / AzureAD, M2M on-behalf-of via
  `SECURITY-PRINCIPAL-ID` / `MSCI-PROFILE-ID`), authorization through OMES/Entitlements with
  fallback to Permission Service (`lib-security`, `lib-omesv2`, `lib-profile`, `lib-iams`).
  Removing or reordering a principal-id or profile-id lookup changes who can see what.
- **Enrichment**: instrument resolution through IRS (`lib-enrichment`,
  `instrument-resolution-client`), with large instrument blobs offloaded to S3 / Azure Blob.
  IRS request-body changes affect sync, async and dry-run paths together.
- **Async import**: `portfolio-experience-service` → RabbitMQ → `portfolio-import-worker-service`,
  job state in the DB via `lib-importjob`, pipeline configuration in `lib-experience-import`.
  Worker-side code has no HTTP request, so see the `TenantContext` note above. Stored job
  response blobs are deserialized later, so older blobs must still read correctly after a
  model change.
- **RSQL** attribute filtering lives in `lib-rsql`.
- **Streaming** endpoints are typed `java.util.stream.Stream<T>` via the generator's
  `schemaMappings`/`typeMappings` and use `http-stream-support`. Streams are lazy: an
  exception thrown inside a spliterator surfaces mid-response, after headers are sent.
- **`portfolio-api-ai`** is an MCP server and the one module that builds a `bootJar`.

## Regression traps specific to this repository

Check each of these against the diff:

- **`TenantContext` not set outside an HTTP request** — jobs, workers, new threads, parallel
  streams, async continuations.
- **Hand-edited generated API sources** — any change under a `*-api-v*` module's generated
  output instead of `api-schema/*.yaml` will be overwritten by the next build.
- **A service depending on `lib-*` instead of `starter-*`** — bypasses auto-configuration and
  works only by accident.
- **A stored-procedure change without a new Liquibase changelog entry** — the proc source is
  updated but never deployed. `runLiquibaseDryRun` must stay green.
- **A read path that does not UNION** `ps.PortfolioSnapshotPosition` with
  `ps.PortfolioSnapshotPositionOverride`, or ignores `isDeleted`.
- **Inlined dependency versions** — versions belong in root `gradle.properties`, referenced
  from build files, with Spring Boot / Spring Cloud version properties or Gradle
  `constraints` (plus a `because` note) for transitives.
- **A changed API model with only some adaptors or converters updated** — check every
  `*ServiceAdaptor*` and `*Converter*` for the model.
- **A shared `lib-*` change with only one consumer verified** — a change in
  `lib-enrichment`, `lib-experience-import` or `lib-common` typically reaches sync, async,
  dry-run and streaming paths at once.
- **Header handling changes** — `SECURITY-TENANT-ID` versus deprecated `X-MSCI-Client-ID`,
  and `MSCI-PROFILE-ID` versus `SECURITY-PRINCIPAL-ID`, have defined precedence. Changing it
  changes tenant resolution for existing callers.

## Tests

- Unit tests are in `src/test` and run with `./gradlew :<module>:test`.
- Integration tests are in the `src/integTest` source set (`integrationTest` task, needs
  docker login).
- **Functional tests live in separate `*-test-functional` modules with sources under
  `src/main/java`, not `src/test`**, and register named `Test` tasks
  (`containerTest`, `containerComponentTest`, `containerSystemTest`, `systemTest`,
  `devPreDeploySanityTest`) instead of using the default `test` task. Tests extend
  `ComponentTest` or `SystemTest`; the target environment comes from the
  `SPRING_BOOT_TEST_CONTAINERS_PROFILE` env var set per Gradle task. Component tests exercise
  the service, controller and data layers in-process; system tests drive the service through
  the Feign clients; sanity tests are tagged `sanity` / `onboard`.
- When assessing coverage, look in all three places. A change with no `src/test` change may
  still be covered by a functional module.
- Builds are not offline-capable (Azure Artifacts feeds, Azure Key Vault, docker login), so
  this workflow does not run them. Base coverage claims on reading tests, and say so.

## Design docs

`docs/content/designs` and `docs/content/decisions` are authoritative for ACLs, benchmarks,
composite portfolios, purging, profiles, RSQL and the experience service. Consult them before
concluding that behaviour in those areas is wrong —
`docs/content/basics/as-at-bitemporal.md` and `docs/content/designs/position-storage.md` in
particular explain the position storage model that a diff alone will not.
