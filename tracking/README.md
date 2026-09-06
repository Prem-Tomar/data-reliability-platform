# Progress rules

The locally retained Excel workbook remains the daily concept tracker. It contains all 765 inherited concepts, including the 361 college audits. The local `concepts.json` is a portable baseline snapshot, not an automatically synchronized copy. Neither inherited file is included in the public repository. Choose the workbook as the authoritative concept record unless you deliberately migrate it. Public-repository users can begin with `DAILY_TEMPLATE.md` and the delivery tracker.

The expanded 64 product packages use `DELIVERY.md`. Launch gates use `docs/LAUNCH_GATES.md`. These three records measure different things and should not be added into one percentage.

## Concept competency

| Level | Meaning | Evidence |
|---|---|---|
| 0 | Not started | No claim |
| 1 | Recognize | Explain the idea with a small example |
| 2 | Apply with help | Complete a guided exercise and describe changes |
| 3 | Independent | Build a changed problem, diagnose a failure and test it |
| 4 | Transfer and review | Apply in a new context, explain trade-offs and pass a delayed recheck |

The workbook retains its own labels and target values. Map these descriptions to the workbook's existing scale before entering values; do not change its validation silently. Core product work targets independent evidence. Breadth electives may stop at guided application. A logged hour, copied implementation or passing test alone does not establish mastery.

## One daily entry

Date; term; subject; concept or package ID; route (college audit/self-study/product); topic; planned hours; actual hours; concept status; commit or artifact; expected versus observed result; blocker; revision date; next action.

Use `DAILY_TEMPLATE.md` for additional product evidence. Avoid entering the same hour in two totals. College study is recorded as college work; the supplementary workload budget counts only additional roadmap work and explicit audits.

## Weekly gate

1. Demonstrate one changed input without copying the lesson.
2. Reproduce one failure and explain its cause.
3. Compare actual hours with the budget. Remove optional work before increasing hours.
4. Audit college coverage using actual notes, assignments and assessment evidence. A brochure mention is not proof of coverage.
5. Review due concepts and one previous product result.
6. Update package evidence, blockers and the next week's three highest-priority actions.

If prerequisites fail, spend the next week repairing them. Do not move every unfinished item into an ever-growing daily backlog. After two missed weekly gates, reduce the next milestone and renegotiate its due date.
