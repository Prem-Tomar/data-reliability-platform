# Repository map

| Location | Purpose |
|---|---|
| `services/ingestion` | Working day-one Python learning seed; evolves into ingestion service |
| `learning` | Subject coaching, first-month schedule and product packages |
| `docs` | Roadmap, architecture, launch gates and source notes |
| `tracking` | Portable concept baseline, delivery checklist and daily template |
| `evidence` | Instructions for dated demonstrations and release evidence |
| `references/original` | Unmodified original spreadsheet, Word and PDF companions |
| `.github/ISSUE_TEMPLATE` | Reusable concept-first learning issue template |

Add each new service only when its milestone begins. At that point give it source, tests, dependency lock, container build, configuration example, migration procedure and runbook. Add versioned API/event schemas to `contracts` when the first boundary is implemented. Add deployment and CI files when their dependencies exist and their checks can actually run.

The production target is documented in architecture and launch gates. Empty service folders and untested deployment manifests are not implementation evidence.
