# Sources and migration notes

Prepared 6 September 2026 from the shared conversation and its locally available generated roadmap artifacts. Final decisions retained: one data reliability product, Python-first project practice, FastAPI, separate language sections, college concepts tracked without duplicate coaching, no IoT, later AI/ML and React last.

## Inherited material

The original generated content contains 765 concept entries, 404 coaching cards and 361 college audit entries across 31 sections. The supplied brochure text and generated content were available locally. College coverage remains an audit hypothesis until actual instruction and assessment evidence confirms it. This is not a newly verified institution-wide syllabus or accreditation mapping.

The local folder retains the original Excel, Word and PDF files unchanged under `references/original`, along with subject Markdown pages reorganizing the inherited coaching fields. These inherited materials and the concept JSON snapshot are excluded from public Git history. Inherited lesson references have not all been individually revalidated. Some inherited examples are generic or terse; the new product packages supply the broader implementation context.

The original workbook's calendar, estimates and 765 concept rows are unchanged. New microservices packages and launch gates use separate Markdown trackers. They do not automatically synchronize with the workbook or JSON snapshots. The new roadmap governs product scope and service sequencing when it differs from the older summary. College dates remain provisional.

## References checked for this expansion

These support specific engineering patterns and learning routes. The 16-term schedule, language choices, workload allocations and acceptance gates are authored planning decisions, not promises made by these sources.

| Reference | Use |
|---|---|
| [Python tutorial](https://docs.python.org/3/tutorial/) | Language reference after introductory coaching; the official tutorial assumes some programming familiarity |
| [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | HTTP APIs, validation, dependency organization and testing |
| [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) | Relational and SQL foundation |
| [Microsoft service data ownership](https://learn.microsoft.com/en-us/dotnet/architecture/microservices/architect-microservice-container-applications/data-sovereignty-per-microservice) | Private domain data per service |
| [AWS transactional outbox](https://docs.aws.amazon.com/en_en/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html) | Reliable state change and event publication pattern |
| [Dagster assets](https://docs.dagster.io/guides/build/assets) | Asset/dependency modelling inspiration |
| [OpenLineage](https://openlineage.io/docs/) | Dataset, job and run lineage concepts |
| [OpenTelemetry signals](https://opentelemetry.io/docs/concepts/signals/) | Logs, metrics and traces |
| [Google SRE workbook](https://sre.google/workbook/implementing-slos/) | User-relevant reliability objectives |
| [scikit-learn pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) | Leakage prevention and consistent preprocessing |
| [PyTorch basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Deep-learning workflow foundations |
| [React Learn](https://react.dev/learn) | Frontend component and state foundation |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Applicable security verification requirements |
| [GitHub secure workflow use](https://docs.github.com/en/actions/reference/security/secure-use?learn=getting_started) | Supply-chain and workflow permission guidance |

Use the search hint in each concept card to find a precise topic. Prefer primary documentation and verify the installed version. Read enough to answer the current question, then return to the exercise. Search results and copied code do not substitute for independent understanding.
