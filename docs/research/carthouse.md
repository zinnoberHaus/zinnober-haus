# Carthouse: research and product direction

Research date: 2026-09-08. Status: proposed architecture and delivery gates; this document does not claim implemented product features. Sources are primary project documentation, repositories, and license texts. Recommendations and targets below are engineering judgments, not measured customer demand or performance results.

## Product thesis

Carthouse should be an open-source, self-hostable data engineering warehouse workbench: connect data, define SQL/Python transformations and AI steps, inspect a DAG, execute it reliably, and query versioned outputs with lineage. Its defining experience should be a reviewable path from an AI-generated proposal to a reproducible data product. The warehouse promise requires actual persisted tables and query access; a graph editor or scheduler alone does not meet it.

The initial customer hypothesis is a small enterprise data platform team that needs private deployment, existing SQL/Python compatibility, and reproducible AI enrichment. Validate that hypothesis with five design partners before expanding the connector catalog. Proposed first use case: ingest order CSVs, validate schema, build daily revenue tables, optionally classify free-text records with a configured model, inspect failed rows, and rerun a partition without duplicating output. A complete non-AI workflow must remain usable without a model account.

## Evidence and alternatives

| Project / layer | Verified capabilities and license | Implication for Carthouse |
| --- | --- | --- |
| [Dagster](https://github.com/dagster-io/dagster) | Asset-oriented orchestration and observation; Apache-2.0. | First orchestration adapter candidate because durable datasets match the product model. Benchmark integration effort before committing. |
| [Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/index.html) | Python-defined batch workflows, dependencies, schedules, monitoring, backfills, and failed-task reruns; Apache project licensing. | Enterprise compatibility adapter and migration path. Reimplementing its scheduler breadth is not an initial differentiator. |
| [Prefect](https://github.com/PrefectHQ/prefect) | Python workflows, retries, caching, schedules, events, self-hosted server; Apache-2.0. | Alternative when dynamic Python control flow is more important than an asset-first model. |
| [DuckDB](https://www.duckdb.org/why_duckdb) | Embedded analytics with extensions including Parquet and object storage protocols; MIT. | Default local query/execution engine and a small installation footprint. |
| [Apache Iceberg](https://iceberg.apache.org/docs/1.10.2/reliability/) | Snapshot-based tables, atomic commits, consistent reads, optimistic concurrent writes, rollback; [Apache repository](https://github.com/apache/iceberg). | Enterprise table format. Requires a catalog, storage, and a compatible compute engine; it is not the scheduler or query server. |
| [Trino](https://trino.io/) | Distributed SQL, federation, multiple data sources, on-premise/cloud deployment; Apache-2.0. | Enterprise query backend. Its [documentation](https://trino.io/docs/current/overview/use-cases.html) explicitly distinguishes analytics queries from a general-purpose transactional database. |
| [dbt Core](https://www.getdbt.com/licenses-faq) | Open-source transformation framework; Core code/binary Apache-2.0. Fusion distribution includes proprietary additions. | Execute user dbt projects through a pinned Core adapter; do not equate a free commercial binary with an open-source dependency. |
| [OpenLineage](https://openlineage.io/docs/) | Standard dataset, job, and run metadata with extensible facets. | Emit interoperable lineage rather than inventing an isolated event vocabulary. |

Current ecosystem changes matter: the [July 13, 2026 Dagster announcement](https://dagster.io/prefect) says it is joining Prefect while retaining its name and open-source license. This supports an adapter boundary rather than assuming independent vendors indefinitely. The [June 2026 dbt licensing FAQ](https://www.getdbt.com/licenses-faq) differentiates Core v2's Apache distribution from proprietary Fusion additions; review the exact artifact shipped, not old summaries of Fusion licensing.

## Architecture boundaries

Use a Python control API/SDK, a browser workbench, and an explicit execution adapter contract. Choose the browser framework through the project ADR workflow. Store operational metadata separately from analytical tables. The following is a recommendation to validate, not a declaration of installed dependencies.

| Boundary | Initial design | Enterprise evolution |
| --- | --- | --- |
| Control plane | Projects, credentials references, versioned DAG specifications, schedules, run records, API, UI | Tenant isolation, OIDC, RBAC, audit export, HA API |
| Orchestration | Carthouse DAG compiler and one upstream adapter; execute through Dagster after a compatibility spike | Adapter for existing Airflow deployments; bounded concurrency and backfill policy |
| Execution | Isolated worker process/container for each SQL/Python/AI task | Customer-network worker pools, resource quotas, cancellation, workload identity |
| Operational state | SQLite for a strictly single-user local profile | PostgreSQL for shared deployments; migration and backup contract |
| Analytical storage | Local persisted DuckDB tables plus portable Parquet exports | Object storage + Iceberg REST catalog; documented engine compatibility matrix |
| Query | DuckDB through a controlled query API | Trino adapter, query authorization, resource groups and query budgets |
| Lineage | Run/job/dataset events and artifact hashes | OpenLineage export, downstream catalog integration |
| AI | Optional model adapter; schema-constrained DAG proposals and explicit AI task nodes | Private model endpoint, approved providers, evaluation and usage controls |

Do not have multiple independent workers write directly to the same embedded DuckDB file. Pin and verify the chosen concurrency model against [DuckDB's current concurrency guidance](https://duckdb.org/docs/current/connect/concurrency.html). Begin with a single writer per database and versioned artifacts; establish separate, tested semantics for the distributed profile. An Iceberg snapshot protects a table commit, not an arbitrary multi-system DAG transaction.

The execution contract must record DAG version, code/container digest, inputs and table snapshots where supported, parameters, partition, attempt, output artifacts, timestamps, and executor identity. Use explicit states: queued, running, succeeded, failed, cancelled. Define retryable errors, timeout and cancellation behavior, dependency failure propagation, and output commit rules. Use idempotency keys for a task/partition/version; assume at-least-once execution and prove that duplicate delivery cannot silently duplicate committed output. A DAG is acyclic; iterative agents run as bounded task internals or explicit successive runs, with maximum steps and spend.

## AI-native means governed execution

The assistant produces a typed DAG and SQL/Python diff, with assumptions and expected outputs. Validation checks schema, cycles, missing inputs, connector capabilities, and policy. Preview uses limited or synthetic data. Authorized users approve promotion according to the deployment's policy; editing a draft need not require approval. Execution uses ordinary workers and the same event records as handwritten pipelines.

Dataset values and retrieved documents are untrusted input, never execution policy. Do not give the model raw secrets or unconstrained shell/database privileges. Scope each task's connections, restrict outbound network access, redact logs, and make external model data transfer configurable. Model invocation records include model identifier, prompt/template version, structured response, evaluation result, latency, and cost when known. Do not promise deterministic regenerated model outputs; retain approved artifacts and outputs needed for replay, subject to retention policy.

Required AI evaluations: valid DAG rate, correct dependency ordering, SQL result correctness on fixtures, injection resistance, credential leakage checks, unauthorized mutation attempts, repair accuracy, and budget enforcement. Report fixture versions and sample counts with results. A compelling demo is useful evidence only when the saved workflow can run without the planning assistant.

## Open-source and enterprise contract

Recommend Apache-2.0 for original Carthouse code, with dependency notices and an inventory of shipped artifacts. It supports redistribution and includes a contributor patent grant; preserve the obligations in the [actual license](https://www.apache.org/licenses/LICENSE-2.0). This is a project licensing recommendation, not a claim that every future connector is compatible. Audit each pinned dependency, model, dataset, and container image; upstream project licensing does not automatically cover commercial extensions or externally hosted services.

Keep the self-hosted product functional without activation, hosted telemetry, or a proprietary model. Publish deployment manifests, configuration schema, migration commands, and export formats. Commercial support or managed hosting can fund the project; basic enterprise security should remain part of the open product promise.

Enterprise readiness requires observable evidence for each item:

| Gate | Required proof |
| --- | --- |
| Installation | Clean Linux Compose install with persistent volumes, deterministic sample, documented resource baseline, no mandatory cloud account |
| Identity and authorization | OIDC integration; positive and negative project/dataset/job permissions tested through API and UI |
| Secrets | Secret references, rotation, log redaction, least-privilege connector credentials |
| Isolation | Cross-project access-denial tests; workers cannot read unrelated credentials or artifacts |
| Durability | Worker/controller crash recovery, duplicate delivery, stale leases, retry limits, cancellation, partition backfill tests |
| Recovery | Backup restored into a new deployment; documented measured RPO/RTO and artifact consistency |
| Upgrades | Supported-version migration and rollback/restore rehearsal, including metadata and tables |
| Operations | Metrics, structured logs, traces, alert examples, run retention, disk/cost quotas |
| Distribution | Pinned release artifacts, SBOM, vulnerability scanning, checksums/signatures, supported dependency matrix |
| Private deployment | Egress-disabled core workflow; private model endpoint; documented network and trust boundaries |

Do not label the product enterprise-ready, compliant, highly available, or exactly-once until the corresponding claims have evidence. No customer certifications or procurement requirements were verified in this research.

## Delivery roadmap and issue-ready acceptance criteria

Milestones are sequential outcome gates, not calendar estimates. Ownership belongs to the Carthouse maintainer and delegated implementation/review agents under the orchestration repository.

1. **CH-001 — Architecture spike and specification.** Compare the same ingestion→SQL→quality-check pipeline using the candidate Dagster adapter and a minimal local executor. Document dependencies, installation cost, cancellation/retry behavior, and data ownership. Publish an ADR selecting the production direction; publish the versioned DAG schema and example. Reject unknown nodes and cycles before execution.
2. **CH-002 — Complete local warehouse path.** Provide a documented install that loads included non-sensitive CSV fixtures, persists queryable tables, displays a DAG/run log, and exports Parquet. Restart and query the same results. Include SQL and Python tasks, validation failure, and failed-node retry. The sample must not require AI or cloud credentials.
3. **CH-003 — Reliable DAG operations.** Scheduling, partition backfills, bounded concurrency, cancellation, retry policy, immutable DAG versions, output commit/idempotency, and lineage. Kill a worker between write and acknowledgment and prove recovery does not duplicate committed rows. Verify dependency failure propagation.
4. **CH-004 — AI-assisted authoring.** Prompt→typed plan→diff→preview→authorized execution, plus an optional enrichment task. Ship fixture-based evaluations and record artifacts. Run the approved graph without the assistant. Verify denial of disallowed SQL, secret access, and outbound calls.
5. **CH-005 — Shared enterprise deployment.** PostgreSQL metadata, OIDC/RBAC/audit, isolated workers, Compose production guidance, Kubernetes manifests, backup/restore, upgrades, resource limits. Pass the enterprise gates above; publish measured capacity rather than invented scale claims.
6. **CH-006 — Open warehouse scale.** Iceberg catalog/storage and Trino adapters, snapshot lineage, engine capability matrix, concurrent-writer recovery tests, query controls, and migration from local artifacts. Demonstrate the same logical data product in both profiles. Unsupported SQL/type behaviors must produce explicit errors.
7. **CH-007 — Ecosystem and stable release.** dbt Core integration, existing Airflow interoperability where demanded, connector SDK, compatibility tests, migration guide, support policy, and reproducible release pipeline. Choose additional connectors from design-partner use, not catalog size.

For the first public repository, publish the architecture, DAG schema, example, runnable local path, tests, contribution guide, security reporting route, license, roadmap, and accurate maturity label. A repository scaffold establishes the project; it does not satisfy the warehouse execution or enterprise gates.

## Outstanding validation

Confirm the most valuable initial data source and enterprise environment with design partners. Benchmark installation time, end-to-end latency, memory, and recovery on disclosed hardware/datasets. Select exact dependency versions only during implementation and retest compatibility at release. Validate connector licensing at the artifact level. Assess the Carthouse name separately before investing in public branding; this research does not establish trademark availability.
