# Four-year learning and product roadmap

## Outcome and teaching model

Build one product from the first day: a platform that connects retailer data sources, detects unreliable data, runs recoverable pipelines and explains results using evidence. Learning concepts and languages is the primary goal. Each feature exists to teach a concept and then demonstrate independent understanding. Customer launch is the final quality bar.

The learning loop is **preview → college or targeted lesson → predict → build → break → diagnose → explain → delayed recheck**. Preview a college topic briefly, use college teaching as its main lesson, and apply it in this project. Keep every college concept in the tracker even when no extra lesson is needed. For a missed or weak concept, repair only the demonstrated gap.

The target architecture is microservices. Learn one component locally before taking on network and delivery failures. Begin with Python ingestion on day one, add separate catalogue and ingestion services in term 3, and evolve service ownership and production controls through later terms. [Architecture](ARCHITECTURE.md) defines the target; [work packages](../learning/PRODUCT_WORK_PACKAGES.md) define the build sequence.

## Product scope

The initial user needs to know: Did my source arrive? Which records are wrong? Did the pipeline finish? Can I rerun it safely? Which records support this result?

The launch scope is three reviewed connector types (CSV, read-only PostgreSQL, HTTP), versioned data contracts, recoverable scheduled jobs, data-quality results, lineage, deterministic retailer insights, and a usable React investigation interface. Forecasts and grounded LLM explanations are released only when their separate evaluation gates pass. Their failure must not disable the core reliability product.

Customer installation means a controlled connector or optional outbound collector with scoped permissions. Start with synthetic systems. A general marketplace for arbitrary executable plugins, unlimited workflow scripting, autonomous data repair, unrestricted LLM tools and dozens of connectors are beyond the first launch.

## Four annual outcomes

| Year | Student outcome | Product evidence |
|---|---|---|
| 1 | Independent Python fundamentals; practical SQL and HTTP; initial C resource understanding | Repeatable file ingestion, two communicating services, validation and source-linked reports |
| 2 | Recovery, service contracts, Java audit, C++/Rust labs and data-science foundations | Durable jobs, three connector contracts, controlled security boundaries and evaluated analytics |
| 3 | Delivery, cloud operations, Go, observability, distributed failures and AI evaluation | Reproducible staging, collector, measured resilience, versioned models and grounded assistance |
| 4 | Accessible React UI, experiments, release engineering and operational handover | Evidence-backed major project, release candidate, controlled launch and maintainable operations |

## Term milestones

Dates are inherited assumptions, not verified institutional deadlines. Weeks are relative to each term. Finish core packages before optional depth; keep weeks 12–13 for review, repair or exams.

| Term | Provisional period | Normal hours/week | Focus | Exit demonstration |
|---|---|---:|---|---|
| T1 | Aug–Oct 2026 | 5 | Python first; recover the missed month | Run a Python ingestion seed and explain every line |
| T2 | Nov 2026–Jan 2027 | 6 | Python structure and data correctness | Release a tested local ingestion component |
| T3 | Feb–Apr 2027 | 7 | FastAPI and the first two services | Catalogue and ingestion communicate over a versioned contract |
| T4 | May–Jul 2027 | 8 | Data quality as a product capability | Explain what is wrong with data and where it came from |
| T5 | Aug–Oct 2027 | 8 | Durable jobs and stronger programming | Persist and recover a workflow with clear ownership |
| T6 | Nov 2027–Jan 2028 | 9 | Reliable asynchronous microservices | Recover from delivery failures without duplicate effects |
| T7 | Feb–Apr 2028 | 10 | Contracts and connector engineering | Connect systems through controlled and testable adapters |
| T8 | May–Jul 2028 | 10 | Analytics and classical ML | Deliver useful analysis with an honest baseline |
| T9 | Aug–Oct 2028 | 11 | Packaging, delivery and platform operations | Reproduce the microservices system in staging |
| T10 | Nov 2028–Jan 2029 | 11 | Customer integration and service observability | Install a bounded connector and investigate failures |
| T11 | Feb–Apr 2029 | 12 | Scale, recovery and model lifecycle | Explain behaviour under load and partial failure |
| T12 | May–Jul 2029 | 12 | Grounded AI assistance | Provide useful explanations with traceable evidence |
| T13 | Aug–Oct 2029 | 12 | Major project scope and pilot readiness | Freeze a defensible product contribution and evaluation plan |
| T14 | Nov 2029–Jan 2030 | 12 | React implementation comes last | Make the working services understandable through the UI |
| T15 | Feb–Apr 2030 | 12 | Release candidate and evidence | Rehearse a real launch and a reproducible major-project submission |
| T16 | May–Jul 2030 | 12 | Launch decision and handover | Complete acceptance and establish a maintainable operating routine |

## Weekly capacity and backlog

The inherited normal weekly budgets are 5, 6, 7, 8, 8, 9, 10, 10, 11, 11, 12, 12, 12, 12, 12, 12 hours. In year 4 use a 6-hour cap while an internship applies. During exams use 25% of the applicable capped budget and focus on revision. Friday is normally rest. Rebalance around the student's real timetable.

First four weeks: 3 hours/week for verified missed college work, 1.5 hours for Python project learning, 0.5 hour for review. Recover the missed month by an independent retest, not by replaying every lecture. If the actual backlog needs more than 12 hours, extend recovery and reduce optional new topics.

After recovery allocate roughly 50% to the current concept and its project exercise, 25% to integration/debugging, 15% to revision and 10% to review/planning. These are parts of the same weekly budget. The 64 packages organize product work already supported by concept learning; they are not 64 additional courses to stack on top.

The inherited plan estimates about 1,509 supplementary hours over four years, with about 655 assigned to concept work. These are estimates, not a guarantee of production mastery. The expanded microservices scope may exceed that capacity. Keep the core launch features; shorten optional languages, advanced ML, additional infrastructure tools and connector breadth when measured progress requires it. Do not silently increase daily hours.

## Prerequisite gates

| Gate | Required independent demonstration | Unlocks |
|---|---|---|
| Python | Write functions using lists/dicts, read a fixture, handle an error, write a useful test, explain a traceback | FastAPI and service code |
| Persistence | Explain keys and transactions; rerun without duplicate effects; inspect a query | Durable jobs and service-owned data |
| Service boundary | Explain timeout vs failure, identity, ownership and API versioning | Asynchronous workflows |
| Distributed delivery | Survive duplicate delivery, worker crash and partial commit; explain limitations | Pilot data ingestion |
| ML foundations | NumPy/data handling, leakage-free splits, linear algebra, derivative/gradient and probability; Java foundation audit per the original preference | Classical ML depth, then deep learning |
| Operations | Reproduce containers, diagnose network/storage issues, restore and roll back | Customer staging/pilot |
| UI | JavaScript/TypeScript, browser HTTP, asynchronous state and stable APIs | React implementation |
| Launch | Exact-release evidence for every mandatory gate | Controlled customer launch |

Java proficiency is a retained educational goal, rather than a technical dependency of Python ML libraries. A failed Java audit gets its own repair plan; do not claim an algorithm mathematically requires Java.

## Language roles and depth

| Subject | Learning role | Project use | Expected depth |
|---|---|---|---|
| Python | First and continuous primary language | Ingestion, FastAPI, workflows, tests, analytics and ML | Independent design, debugging and maintenance |
| Java | College-led, audited with project evidence | Read-only enterprise inventory adapter | Independent foundations; integration when justified |
| C | Memory and machine-level reasoning | Bounded record-parser lab inside the product | Explain pointers, bounds and resource failure |
| C++ | Lifetime and resource abstraction | Batch-processing lab using RAII | Independent lab with comparative evidence |
| Rust | Ownership and typed failure | Optional validated parser component | Safe lab; production integration requires measured benefit |
| Go | Concurrency and cancellation | Optional outbound customer collector | Independently test bounded concurrent behaviour |
| SQL | Data semantics and durability | Private service stores, validation and analytics | Independent query correctness and transaction reasoning |
| JavaScript/TypeScript | Browser and frontend foundations | React investigation interface late in the plan | Independent UI state and API integration |
| Haskell | Small conceptual elective | Pure transformations and folds | Maximum six-hour comparative exercise |

Separate subject libraries prevent a long mixed checklist. The calendar still controls prerequisites and due work. A language lab can remain in the repository without becoming a production microservice. Service boundaries follow business ownership, not the number of languages studied.

## AI/ML and data-science breadth

Proceed through maths and statistics; Python/NumPy/dataframes; data cleaning and EDA; supervised and unsupervised classical ML; model selection and calibration; time-series forecasting and anomalies; neural networks and backpropagation; embeddings and transformers; retrieval and LLM evaluation; model serving and monitoring. Cover leakage, uncertainty, temporal splits, class imbalance, experiment reproducibility and responsible interpretation throughout.

Computer vision, reinforcement learning and advanced architectures remain visible in the subject checklist and bounded experiments. Product integration needs a credible use case and a baseline comparison. Exhaustive awareness of a field is different from equal mastery of every subfield. Advanced breadth must not displace the core reliability and release work.

## Major project and launch

Confirm the actual supervisor rubric and submission dates at the next opportunity, then review formally in T13. Prepare the submission candidate in T15; move the work earlier if the institution requires it. Preserve proposal, related work, requirements, architecture decisions, implementation evidence, tests, experiments, limitations, report, demo and viva notes.

Potential experiments compare unsafe vs idempotent replay, simple retry vs outbox delivery, batch sizes vs throughput/memory, quality checks vs injected defects, models vs seasonal baselines, retrieval-only vs LLM explanations, and user investigation time before/after the interface. Never inject faults into an unapproved customer environment.

Use [launch gates](LAUNCH_GATES.md) for the product release and the college rubric for academic acceptance. Passing one does not imply passing the other.
