# Launch acceptance

All gates below are **unverified**. This repository currently provides learning material and a starter component. These are future release checks, not claims of production readiness.

Before a pilot, agree the load envelope, response-time targets, freshness target, allowable recovery time (RTO), allowable data loss (RPO), retention period, cost budget and named operating owner. Use measured evidence to set realistic targets; do not insert arbitrary production promises.

An illustrative local test might use 100,000 synthetic orders, 10 concurrent run requests and a 10-minute worker outage. That is a learning scenario, not a customer capacity commitment. Define the actual pilot workload and success thresholds before its validation run.

Every mandatory gate needs a procedure, result, exact release candidate, reviewer and dated evidence. L18/L19 may be marked not applicable only if those features are disabled and absent from launch claims. A feature flag alone does not waive shared security and data-handling obligations.

| Complete | ID | Gate | Acceptance procedure | Evidence / reviewer / date |
|---|---|---|---|---|
| [ ] | L01 | Product scope | Run CSV orders, database inventory and HTTP ticket ingestion through validation, report and source drill-down. Document supported limits and excluded features. | |
| [ ] | L02 | Tenant isolation | Test cross-tenant object IDs, lists, downloads, caches, event injection and AI retrieval. Every forbidden path is denied without leaking another tenant's data. | |
| [ ] | L03 | Identity and access | Verify authentication, roles, expiry/revocation, service identity, restricted connector permissions and authorization at each service boundary. | |
| [ ] | L04 | Secret handling | Verify secrets are absent from Git, logs and output artifacts; demonstrate rotation and a documented response for exposed credentials. | |
| [ ] | L05 | Connector safety | Pass conformance tests for all launched connectors, including size limits, timeouts, network destination restrictions, schema drift, revocation and uninstall. | |
| [ ] | L06 | Correctness | Match hand-checked fixtures for currency, timestamps, duplicates, missing rows, invalid values and join cardinality. Report accepted, quarantined and dropped counts explicitly. | |
| [ ] | L07 | Replay and durability | Crash workers at documented commit/publish/checkpoint boundaries and replay partitions. Reconcile accepted source identities and final output without duplicate business effects. | |
| [ ] | L08 | Workflow control | Verify schedule overlap policy, cycle rejection, retry limits, cancellation races, lease expiry and dead-letter inspection/replay. | |
| [ ] | L09 | Schema compatibility | Test supported old/new producers and consumers, database expansion/migration and rollback or forward-recovery procedures using seeded data. | |
| [ ] | L10 | Lineage and reproducibility | Trace a selected insight to input snapshot, rows, transformations, rules and code version. Reproduce the result from retained authorized inputs. | |
| [ ] | L11 | Restore | Restore metadata and artifact manifests in isolation, reconcile cross-service state, and measure actual recovery time and data loss against the approved RTO/RPO. | |
| [ ] | L12 | Load and limits | Run the agreed pilot workload and a stress case. Publish throughput, p95 latency, queue lag, memory and error rates with hardware, input sizes and duration. | |
| [ ] | L13 | Telemetry and alert response | Inject a stale feed and a failed job. Observe actionable alerts, trace investigation and correct owner response without sensitive data in telemetry. | |
| [ ] | L14 | Delivery and rollback | Deploy the tested immutable release, execute migrations and smoke tests, then rehearse rollback. Verify no undocumented manual environment changes. | |
| [ ] | L15 | Security review | Complete applicable ASVS requirements, dependency/container checks and abuse-case tests. Resolve critical/high findings before launch unless a documented review establishes they are inapplicable. | |
| [ ] | L16 | Privacy and lifecycle | Document data inventory, purpose, permissions, retention and deletion. Test tenant deletion across stores, artifacts and derived results with a documented backup retention exception. | |
| [ ] | L17 | Frontend usability | Pass keyboard and accessible-name checks and end-to-end source setup, failed-run investigation and evidence drill-down. Cover loading, empty, error and session expiry. | |
| [ ] | L18 | ML acceptance when enabled | Publish time-aware holdout results, baseline comparison, slice metrics, training lineage, limitations and rollback. Do not enable models that fail the agreed usefulness threshold. | |
| [ ] | L19 | LLM acceptance when enabled | Evaluate authorization, grounding, citations, prompt injection, abstention, latency and cost on a frozen set. Keep deterministic reporting available when the model is unavailable. | |
| [ ] | L20 | Operations and economics | Assign support and incident ownership, pilot resource budget, maintenance schedule and escalation. Have a second person perform onboarding and one recovery procedure. | |
| [ ] | L21 | Release decision | Record exact commit/artifact digests, all gate evidence, outstanding accepted limitations, rollout steps, rollback triggers and named reviewer go/no-go. | |

Do not approve a release from one successful happy-path demo. If a gate fails, record the observed failure and the smallest repair. Recheck affected gates after code, schema, dependency or infrastructure changes. Keep academic submission acceptance separate from customer release acceptance.
