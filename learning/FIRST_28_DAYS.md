# First 28 days

Day 1 is the chosen restart day. The inherited suggestion is 7 September 2026; change it to the student's actual start. The first month has 5 supplementary hours/week: 3 hours of real college backlog, 1.5 hours of Python project practice and 0.5 hour of review. Do not add these hours on top of a second roadmap allocation.

## Twelve Python sessions

Each Python session is 30 minutes: 5 minutes recall/prediction, 10 minutes explanation and experiment, 10 minutes project work, 5 minutes evidence. A difficult session may repeat in the next slot. The goal is understanding, not finishing the calendar.

| Week | Monday, 30 min | Wednesday, 30 min | Saturday, 30 min |
|---|---|---|---|
| 1 | Run `services/ingestion/main.py`; identify input, operation and output | Change quantity and unit price; predict before running | Explain variable names, integer values and assignment; save a changed example |
| 2 | Compare integer `2` with string `"2"`; observe what changes | Add a second synthetic order using distinct variables | Add order totals and deliberately repair an incorrect expression |
| 3 | Introduce `if` and boolean comparisons for quantity validation | Introduce a small function returning a result; distinguish return from print | Test a valid, zero and negative quantity; explain the boundary policy |
| 4 | Store two orders in a list of dictionaries and inspect fields | Loop over records, validating each and counting accepted/rejected | Demonstrate a changed fixture independently and explain one failure |

If functions or loops are too large a jump, spend week 4 consolidating variables and conditions and continue the second issue in the following month. The first issue is about confidence with values; the second introduces structured validation over multiple sessions.

## All 28 daily slots

Repeat the following seven-day pattern for four weeks. Review decides which actual missed college topic occupies each backlog slot.

| Day in each week | Supplementary activity | Time |
|---|---|---:|
| Monday | Python session | 0.5 h |
| Tuesday | Highest-priority college backlog prerequisite | 1.0 h |
| Wednesday | Python session | 0.5 h |
| Thursday | College exercise and independent retest | 1.0 h |
| Friday | Rest | 0 h |
| Saturday | Python session plus college backlog | 1.5 h |
| Sunday | Evidence review and next-week plan | 0.5 h |

Total: 5 hours/week, 20 hours across four weeks. Normal college classes and assigned work remain separate. If the additional backlog load is not sustainable, extend recovery instead of removing rest.

## Backlog coaching

Week 1: inventory the missed classes and assignments; test prerequisites with one small problem per important topic. Do not infer weaknesses just because a class was missed.

Week 2: repair the most blocking topic, use college notes and complete a changed exercise. Preserve the before/after explanation.

Week 3: repair the next prerequisite and retest week 1's repaired topic without notes.

Week 4: demonstrate the remaining critical work and list unresolved items. Close the backlog only when the independent checks pass. The plan reserves 12 hours, not a guarantee that all missed work fits.

## Lesson: variables and order totals

A variable is a name associated with a value. `quantity = 2` associates the name with the integer 2. `quantity * unit_price_paise` computes a new integer. `print` displays a value so you can inspect it.

The starter stores money in paise, the smaller whole-number unit, so the arithmetic does not need decimal fractions. Two items at 12,500 paise cost 25,000 paise. This first example assumes one currency; later the platform must record currency and rounding rules explicitly.

Before changing `quantity` to 3, write the expected result: 37,500 paise. Run it, compare the output and explain any difference. Then change one variable at a time. Record the prediction as well as the final output.

Debugging exercise: change the quantity to the text `"2"`. Explain why multiplying text by an integer behaves differently from numeric multiplication. Restore the integer. Do not copy a type-conversion fix until you can describe what conversion means.

## Lesson: functions and validation

A function gives a name to a reusable operation. A parameter is the input name inside the function. `return` sends the result back to the caller. `print` only displays it. Keeping calculation separate from display makes it easier to test.

A boolean condition answers a yes/no question. For this exercise define the rule explicitly: quantity must be an integer greater than zero. Decide why zero belongs on one side of the boundary before writing the condition. Later add price validation, error reasons and rejected-record storage.

Build `calculate_total(quantity, unit_price_paise)` and test inputs by hand. Then build validation separately. Do not add FastAPI or a database to solve a function exercise. Those tools arrive when the prerequisite checks pass.

## Evidence required

For each completed session save the date, concept, predicted output, actual output, code/commit and one sentence explaining the governing rule. For each week show one changed example and one investigated failure. Start with the [daily template](../tracking/DAILY_TEMPLATE.md).
