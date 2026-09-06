# Product work packages

Each package links concept learning to one bounded improvement in the same product. Complete packages in prerequisite order. Suggested due windows are term weeks 3, 6, 9 and 11. Weeks 12–13 are reserved for repair/review/exams. During a six-hour internship cap reduce optional depth, not evidence quality.

For each package: first explain the concepts and predict a small example; implement the smallest useful feature; deliberately exercise the stated failure; diagnose it; demonstrate a changed input without copying; record evidence and a delayed revision date. Each subject card supplies more detailed concept explanations.

## Term 1 — Python first; recover the missed month

**Exit demonstration:** Run a Python ingestion seed and explain every line.

### P001 — Python execution and values

**Learn:** variables, strings, integers, expressions, terminal and editor.

**Build:** Change the day-one order quantity, predict the total, run the seed and save the result.

**Acceptance evidence:** A changed input produces the predicted integer total; explain why money uses paise.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T1, week 3. **Status:** not started.

### P002 — Decisions and repetition

**Learn:** booleans, branches, loops, lists and dictionaries.

**Build:** Process a small in-memory order list and separate invalid quantities.

**Acceptance evidence:** Zero and negative quantities follow a deliberate rule; all rows are accounted for.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T1, week 6. **Status:** not started.

### P003 — Functions and debugging

**Learn:** parameters, return values, scope, tracebacks and assertions.

**Build:** Extract order validation from reporting and diagnose a deliberately wrong comparison.

**Acceptance evidence:** A new invalid input fails before the repair and follows the intended rule afterwards.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T1, week 9. **Status:** not started.

### P004 — Files and first project release

**Learn:** paths, text encoding, JSON, CSV, Git and README.

**Build:** Load synthetic orders from a file and save accepted and rejected counts.

**Acceptance evidence:** A clean local checkout reproduces the report; malformed input has an explicit failure.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T1, week 11. **Status:** not started.

## Term 2 — Python structure and data correctness

**Exit demonstration:** Release a tested local ingestion component.

### P005 — Maintainable Python

**Learn:** modules, packages, type hints, dataclasses and exceptions.

**Build:** Separate parsing, validation, aggregation and command-line concerns.

**Acceptance evidence:** Importing a module performs no data writes; errors preserve useful context.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T2, week 3. **Status:** not started.

### P006 — Persistent data foundation

**Learn:** SQL, keys, constraints, transactions and parameterized queries.

**Build:** Persist source records and run metadata with unique source-record identifiers.

**Acceptance evidence:** Rerunning an identical input does not inflate accepted totals.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T2, week 6. **Status:** not started.

### P007 — Trustworthy transformations

**Learn:** decimal arithmetic, currency, time zones, joins and deterministic functions.

**Build:** Build daily sales and cancellation summaries from immutable synthetic input.

**Acceptance evidence:** Hand-computed fixture totals match; a join cannot silently multiply orders.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T2, week 9. **Status:** not started.

### P008 — Test and design the first user journey

**Learn:** unit tests, integration tests, fixtures and interface sketches.

**Build:** Test boundaries and sketch source registration, run inspection and report evidence.

**Acceptance evidence:** A learner explains one test that catches a real regression and demos input-to-report.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T2, week 11. **Status:** not started.

## Term 3 — FastAPI and the first two services

**Exit demonstration:** Catalogue and ingestion communicate over a versioned contract.

### P009 — Catalogue API

**Learn:** HTTP methods, validation, schemas, errors and dependency injection.

**Build:** Build FastAPI source registration and run lookup with a generated API description.

**Acceptance evidence:** Valid and invalid requests have stable documented responses.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T3, week 3. **Status:** not started.

### P010 — First microservices boundary

**Learn:** processes, network failure, timeouts and service ownership.

**Build:** Run catalogue and ingestion separately; each owns its data and credentials.

**Acceptance evidence:** Stopping ingestion leaves catalogue reads responsive with truthful run state.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T3, week 6. **Status:** not started.

### P011 — Durable run requests

**Learn:** job identifiers, idempotency keys, persistence and polling.

**Build:** Store a run request before execution and return a status resource.

**Acceptance evidence:** A client retry refers to the same intended run and cannot enqueue uncontrolled duplicates.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T3, week 9. **Status:** not started.

### P012 — C parsing lab

**Learn:** compilation, integer bounds, arrays, pointers and file errors.

**Build:** Parse a bounded synthetic record in a C lab and compare with the Python contract.

**Acceptance evidence:** Malformed and oversized records fail safely; compiler diagnostics are investigated.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T3, week 11. **Status:** not started.

## Term 4 — Data quality as a product capability

**Exit demonstration:** Explain what is wrong with data and where it came from.

### P013 — Validation and quarantine

**Learn:** schema, nulls, uniqueness, ranges and reason codes.

**Build:** Add a quality component with versioned rules and a reviewable quarantine.

**Acceptance evidence:** Every rejected row has source identity and a precise rule result.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T4, week 3. **Status:** not started.

### P014 — Lineage and reproducibility

**Learn:** dataset, job, run, artifact version and provenance.

**Build:** Record source-to-output links and code/rule versions for each report.

**Acceptance evidence:** Trace a report value to source rows and reproduce the same result.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T4, week 6. **Status:** not started.

### P015 — Freshness and reconciliation

**Learn:** event time, ingestion time, freshness, completeness and reconciliation.

**Build:** Distinguish a healthy empty feed from a missing or late feed.

**Acceptance evidence:** Injected staleness and missing records are detected without corrupting a valid empty day.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T4, week 9. **Status:** not started.

### P016 — C resource discipline

**Learn:** allocation, lifetime, bounds checking and memory diagnostics.

**Build:** Extend the parsing lab with bounded allocation and systematic cleanup.

**Acceptance evidence:** Representative malformed input runs show no diagnosed leaks or out-of-bounds access.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T4, week 11. **Status:** not started.

## Term 5 — Durable jobs and stronger programming

**Exit demonstration:** Persist and recover a workflow with clear ownership.

### P017 — Workflow state machine

**Learn:** states, legal transitions, attempts, leases and cancellation.

**Build:** Model queued, running, succeeded, failed and cancelled attempts.

**Acceptance evidence:** Illegal transitions fail and cancellation has a documented race policy.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T5, week 3. **Status:** not started.

### P018 — SQL ownership and migrations

**Learn:** indexes, isolation, migrations, locking and query plans.

**Build:** Give each service private database access and version its schema.

**Acceptance evidence:** No service reads another service table directly; upgrade a seeded database safely.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T5, week 6. **Status:** not started.

### P019 — Java integration audit

**Learn:** classes, interfaces, collections, exceptions, JDBC and testing.

**Build:** After college instruction, write a read-only inventory adapter implementing a contract.

**Acceptance evidence:** A changed inventory fixture is processed independently with safe query parameters.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T5, week 9. **Status:** not started.

### P020 — C++ processing lab

**Learn:** references, const, value semantics, RAII and containers.

**Build:** Build a bounded C++ batch summary over the same synthetic records.

**Acceptance evidence:** Resources release on failure; compare accuracy and trade-offs with Python.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T5, week 11. **Status:** not started.

## Term 6 — Reliable asynchronous microservices

**Exit demonstration:** Recover from delivery failures without duplicate effects.

### P021 — Broker and backpressure

**Learn:** queues, acknowledgements, redelivery, bounded concurrency and retries.

**Build:** Move run execution to a durable broker with capped attempts and dead-letter handling.

**Acceptance evidence:** A failed worker triggers bounded redelivery without unbounded queue growth.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T6, week 3. **Status:** not started.

### P022 — Outbox and inbox

**Learn:** local transactions, outbox relay, consumer deduplication and ordering.

**Build:** Commit state plus an outbox event together and deduplicate consumer effects.

**Acceptance evidence:** Crashes before publish and after commit do not lose accepted work or double-apply effects.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T6, week 6. **Status:** not started.

### P023 — Workflow dependencies

**Learn:** directed acyclic graphs, cycle detection, partitions and backfills.

**Build:** Execute a small ingest-validate-transform workflow with partition-aware replay.

**Acceptance evidence:** Cycles are rejected and replay updates only the intended partition.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T6, week 9. **Status:** not started.

### P024 — Security foundation

**Learn:** identity, authorization, least privilege, secrets and threat modelling.

**Build:** Integrate a maintained identity provider and enforce roles and tenant scope in services.

**Acceptance evidence:** Tenant A cannot enumerate, fetch or modify tenant B objects using guessed identifiers.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T6, week 11. **Status:** not started.

## Term 7 — Contracts and connector engineering

**Exit demonstration:** Connect systems through controlled and testable adapters.

### P025 — Connector contract

**Learn:** configuration schemas, capabilities, cursor checkpoints and versioning.

**Build:** Define discover, test-connection and read-batch operations with a connector test suite.

**Acceptance evidence:** CSV, database and HTTP fixtures follow one result and error contract.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T7, week 3. **Status:** not started.

### P026 — HTTP connector reliability

**Learn:** pagination, rate limits, timeouts, credentials and schema drift.

**Build:** Read a synthetic support API with checkpoint resume and bounded page handling.

**Acceptance evidence:** A repeated page, expired cursor and response schema change produce deliberate outcomes.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T7, week 6. **Status:** not started.

### P027 — Rust validator lab

**Learn:** ownership, borrowing, enums, Result, traits and property tests.

**Build:** Write a typed record validator and compare errors with the Python reference.

**Acceptance evidence:** Changed invalid inputs return typed errors; integrate only with correctness and measured benefit.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T7, week 9. **Status:** not started.

### P028 — Programming and maths readiness

**Learn:** Python data handling, Java foundations, linear algebra, calculus and probability.

**Build:** Complete independent prerequisite checks using platform fixtures.

**Acceptance evidence:** Explain train/test separation, a gradient and conditional probability before advanced ML.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T7, week 11. **Status:** not started.

## Term 8 — Analytics and classical ML

**Exit demonstration:** Deliver useful analysis with an honest baseline.

### P029 — Exploratory data analysis

**Learn:** dataframes, missingness, distributions, sampling and descriptive statistics.

**Build:** Investigate cancellations by source, product and time without overstating causes.

**Acceptance evidence:** The report distinguishes observations, hypotheses and missing evidence.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T8, week 3. **Status:** not started.

### P030 — Classical models

**Learn:** linear/logistic regression, trees, ensembles, clustering and dimensionality reduction.

**Build:** Compare appropriate models on a frozen cancellation or anomaly task.

**Acceptance evidence:** Training transformations fit only training data; metrics include class imbalance effects.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T8, week 6. **Status:** not started.

### P031 — Forecasting and anomaly evaluation

**Learn:** time splits, seasonal baselines, residuals, precision and recall.

**Build:** Compare a demand forecast with a seasonal naive baseline and assess alert usefulness.

**Acceptance evidence:** Temporal holdout and slice metrics are reproducible; a worse model is not promoted.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T8, week 9. **Status:** not started.

### P032 — Data product evidence

**Learn:** metric definitions, dataset versions, model cards and uncertainty.

**Build:** Publish versioned deterministic insights plus an experimental ML result.

**Acceptance evidence:** Every output identifies its input version and limitations; deterministic reports work without ML.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T8, week 11. **Status:** not started.

## Term 9 — Packaging, delivery and platform operations

**Exit demonstration:** Reproduce the microservices system in staging.

### P033 — Containers and local deployment

**Learn:** Linux processes, image builds, networking, volumes and health checks.

**Build:** Package implemented services and dependencies in a reproducible local composition.

**Acceptance evidence:** A fresh machine can start the documented subset and preserve expected data across restart.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T9, week 3. **Status:** not started.

### P034 — Continuous integration

**Learn:** dependency locks, contract tests, migration checks, artifact digests and supply chain.

**Build:** Build and verify service artifacts on changes with minimal workflow permissions.

**Acceptance evidence:** A contract-breaking change blocks release and the tested artifact is the deployed artifact.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T9, week 6. **Status:** not started.

### P035 — Infrastructure as code

**Learn:** cloud primitives, Terraform state, plans, drift and teardown.

**Build:** Provision a small isolated staging environment with budget ownership and documented teardown.

**Acceptance evidence:** Recreate the environment without manual hidden settings and record its resource inventory.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T9, week 9. **Status:** not started.

### P036 — Kubernetes lab

**Learn:** deployments, services, probes, requests, limits and rolling updates.

**Build:** Operate one existing service in a bounded cluster lab after container readiness.

**Acceptance evidence:** Diagnose an unhealthy deployment and roll it back; adopt for pilot only if operations justify it.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T9, week 11. **Status:** not started.

## Term 10 — Customer integration and service observability

**Exit demonstration:** Install a bounded connector and investigate failures.

### P037 — Go collection agent

**Learn:** packages, interfaces, goroutines, channels, contexts and cancellation.

**Build:** Build an optional outbound-only collector with bounded concurrency and buffered retry.

**Acceptance evidence:** Offline recovery drains its bounded spool without duplicates; cancellation stops work.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T10, week 3. **Status:** not started.

### P038 — Customer connector lifecycle

**Learn:** installation, scoped credentials, upgrade, revocation and removal.

**Build:** Package one reviewed connector with onboarding and uninstall instructions.

**Acceptance evidence:** Revoked access stops collection; an upgrade preserves checkpoints; removal leaves no active credential.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T10, week 6. **Status:** not started.

### P039 — End-to-end observability

**Learn:** structured logs, metrics, traces, correlation and cardinality.

**Build:** Trace API request, queued task, validation and output across services.

**Acceptance evidence:** Investigate an injected failure using one run identifier without logging record contents.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T10, week 9. **Status:** not started.

### P040 — Data reliability objectives

**Learn:** SLIs, SLOs, freshness, alerting and error budgets.

**Build:** Define user-relevant service and data objectives with an alert response guide.

**Acceptance evidence:** A stale feed alerts the correct owner; API health does not hide stale data.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T10, week 11. **Status:** not started.

## Term 11 — Scale, recovery and model lifecycle

**Exit demonstration:** Explain behaviour under load and partial failure.

### P041 — Performance and resilience

**Learn:** profiling, capacity, load testing, queue lag and failure injection.

**Build:** Measure bottlenecks and test slow consumers, restarts and dependency outages.

**Acceptance evidence:** Published p95, throughput and recovery results name hardware and exact workload.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T11, week 3. **Status:** not started.

### P042 — Recovery and data lifecycle

**Learn:** backups, restore, retention, deletion and reconciliation.

**Build:** Restore service data and artifacts into an isolated environment and reconcile runs.

**Acceptance evidence:** Measured recovery meets proposed RPO/RTO; deletion and retention are tested across derived data.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T11, week 6. **Status:** not started.

### P043 — Model serving and MLOps

**Learn:** model registry, training lineage, drift, champion/challenger and rollback.

**Build:** Version and serve a model behind an evaluated service contract.

**Acceptance evidence:** A bad candidate rolls back and unavailable serving falls back to deterministic reporting.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T11, week 9. **Status:** not started.

### P044 — Deep learning track

**Learn:** tensors, autograd, backpropagation, optimization and regularization.

**Build:** Train a small PyTorch model on a justified platform task and compare with classical methods.

**Acceptance evidence:** Explain a gradient, reproduce a run and reject added complexity without measured benefit.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T11, week 11. **Status:** not started.

## Term 12 — Grounded AI assistance

**Exit demonstration:** Provide useful explanations with traceable evidence.

### P045 — Retrieval and text engineering

**Learn:** tokenization, embeddings, indexing, retrieval and access filtering.

**Build:** Retrieve only authorized incident notes and metric definitions for an investigation.

**Acceptance evidence:** Cross-tenant documents never enter retrieval context; source links resolve.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T12, week 3. **Status:** not started.

### P046 — LLM explanations

**Learn:** structured output, citations, uncertainty, abstention and prompt injection.

**Build:** Generate explanations from computed facts and retrieved evidence.

**Acceptance evidence:** Unsupported claims trigger abstention or review; untrusted text cannot authorize actions.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T12, week 6. **Status:** not started.

### P047 — AI evaluation and efficiency

**Learn:** frozen evaluation sets, caching, token budgets, latency and cost.

**Build:** Evaluate groundedness, factual consistency, access filtering and usefulness.

**Acceptance evidence:** Publish error examples and per-investigation cost; deterministic alternatives remain available.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T12, week 9. **Status:** not started.

### P048 — Advanced AI breadth

**Learn:** transformers, time-series models, NLP, computer vision and reinforcement learning.

**Build:** Use bounded offline experiments relevant to ticket text or pipeline scheduling.

**Acceptance evidence:** Explain applicability and failure modes; keep CV/RL elective unless product evidence justifies them.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T12, week 11. **Status:** not started.

## Term 13 — Major project scope and pilot readiness

**Exit demonstration:** Freeze a defensible product contribution and evaluation plan.

### P049 — Major project proposal

**Learn:** problem formulation, literature comparison, novelty and evaluation design.

**Build:** Confirm supervisor rubric and deadlines; define the research and engineering contribution.

**Acceptance evidence:** Approved scope names testable questions and maps report sections to evidence.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T13, week 3. **Status:** not started.

### P050 — Pilot scope and usability design

**Learn:** personas, task flows, onboarding, accessibility and information architecture.

**Build:** Test sketches for source setup, failed-run investigation and insight-to-source navigation.

**Acceptance evidence:** Representative users can explain the next action from each screen.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T13, week 6. **Status:** not started.

### P051 — Launch threat and operations review

**Learn:** risk review, support ownership, security verification and incident response.

**Build:** Review applicable security requirements and rehearse one complete incident.

**Acceptance evidence:** Each launch gate has an owner and procedure; unresolved critical risks block customer use.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T13, week 9. **Status:** not started.

### P052 — Elective consolidation

**Learn:** Haskell pure functions, types, higher-order functions and folds.

**Build:** Spend at most six hours comparing pure transformations with Python pipeline functions.

**Acceptance evidence:** Explain the concept and one trade-off; move unused time to prerequisite repair.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T13, week 11. **Status:** not started.

## Term 14 — React implementation comes last

**Exit demonstration:** Make the working services understandable through the UI.

### P053 — JavaScript and TypeScript gate

**Learn:** modules, promises, types, browser HTTP and state.

**Build:** Complete browser-language exercises against stable catalogue and run APIs.

**Acceptance evidence:** Handle failed and cancelled requests without stale or misleading results.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T14, week 3. **Status:** not started.

### P054 — React product foundation

**Learn:** components, state, routing, forms and accessibility.

**Build:** Build source setup, run history and quality summary views.

**Acceptance evidence:** Keyboard-only onboarding succeeds and field errors identify a useful correction.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T14, week 6. **Status:** not started.

### P055 — Interactive investigation

**Learn:** graph views, drill-down, comparisons, timelines and chart semantics.

**Build:** Build pipeline inspection, run comparison and insight-to-source navigation.

**Acceptance evidence:** A chart point resolves to supporting records and a failed node resolves to a diagnostic.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T14, week 9. **Status:** not started.

### P056 — Frontend quality and integration

**Learn:** component tests, end-to-end tests, loading/empty/error states and budgets.

**Build:** Exercise the complete retailer journey with auth and real staging service contracts.

**Acceptance evidence:** Refresh, slow network and expired sessions preserve truthful state and recoverable navigation.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T14, week 11. **Status:** not started.

## Term 15 — Release candidate and evidence

**Exit demonstration:** Rehearse a real launch and a reproducible major-project submission.

### P057 — Feature freeze and release validation

**Learn:** compatibility, migrations, security fixes and regression selection.

**Build:** Freeze candidate scope and run all applicable launch gate procedures.

**Acceptance evidence:** All mandatory gates have dated evidence for the exact release candidate.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T15, week 3. **Status:** not started.

### P058 — Pilot and operational rehearsal

**Learn:** onboarding, support, alert response, rollback and cost review.

**Build:** Onboard an approved pilot environment and rehearse failure, restore and rollback.

**Acceptance evidence:** A second person follows the runbook without undocumented intervention.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T15, week 6. **Status:** not started.

### P059 — Experiments and report

**Learn:** baselines, ablations, reproducibility, limitations and technical writing.

**Build:** Finish reliability, performance, ML and usability experiments and write the report.

**Acceptance evidence:** Each claimed result links to a reproducible experiment and acknowledges limitations.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T15, week 9. **Status:** not started.

### P060 — Submission and viva preparation

**Learn:** demonstration, architecture defence, test interpretation and handover.

**Build:** Rehearse a clean-environment demo and answer why each service and language exists.

**Acceptance evidence:** Candidate matches the actual college rubric and the confirmed submission deadline.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T15, week 11. **Status:** not started.

## Term 16 — Launch decision and handover

**Exit demonstration:** Complete acceptance and establish a maintainable operating routine.

### P061 — Final acceptance

**Learn:** release review, outstanding defects and go/no-go decision.

**Build:** Resolve mandatory gate failures and record the release decision.

**Acceptance evidence:** Named reviewer accepts the exact version; unpassed gates remain visible.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T16, week 3. **Status:** not started.

### P062 — Controlled launch

**Learn:** staged rollout, smoke tests, rollback triggers and user communication.

**Build:** Launch only the approved pilot scope and monitor agreed objectives.

**Acceptance evidence:** Rollout can stop safely; customer-facing claims match measured behaviour.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T16, week 6. **Status:** not started.

### P063 — Maintenance and ownership

**Learn:** patching, restore cadence, incident review, cost control and support.

**Build:** Hand over operating ownership with a recurring maintenance calendar.

**Acceptance evidence:** A new maintainer handles one upgrade and recovery rehearsal.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T16, week 9. **Status:** not started.

### P064 — Portfolio and next learning plan

**Learn:** architecture explanation, evidence curation and reflective review.

**Build:** Prepare a sanitized project narrative, demo and next-term improvement backlog.

**Acceptance evidence:** Explain trade-offs and measured outcomes without exposing customer data.

**Coach check:** Explain the governing concept, show one useful failure, then solve a changed example. If an API or library detail is unfamiliar, read its official reference and explain the chosen behaviour before integrating it.

**Due:** T16, week 11. **Status:** not started.
