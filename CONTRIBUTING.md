# Contributing

Keep one change focused on one learning outcome or product capability. Identify its term, package and prerequisite. Explain the user-visible behaviour, failure behaviour and evidence. Use synthetic data. Record sources and dependency versions. Do not mark a production gate complete from a local demonstration.

Service changes must preserve ownership boundaries and include relevant unit, integration, contract, authorization and recovery checks. API or event changes need compatibility evidence. Performance claims need a reproducible workload and baseline. Keep migration and rollback instructions with the change.

## Branch and review workflow

Create a task branch and open a pull request into master. All changes to master go through PR merges. Never force-push published work; use corrective commits. Only the human owner, Prem-Tomar, has a force-push exception. Agents must not use it, even through the owner's credentials. See AGENTS.md for the persistent agent policy.
