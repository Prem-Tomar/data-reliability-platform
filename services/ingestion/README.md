# Ingestion learning component

This is the first working piece of the future ingestion service. Begin with `main.py`, which uses only Python's standard features and synthetic values.

From the repository root run:

```console
python services/ingestion/main.py
```

Expected output:

```text
Order: ORDER-001
Quantity: 2
Total (paise): 25000
```

If your Windows Python command is `py`, use `py services/ingestion/main.py`. Confirm the command selects Python 3. No framework, database or container is needed for this first exercise.

The values intentionally start directly in the script. Learn variables and arithmetic, then evolve this same component into functions, lists of records, validation, file parsing and eventually a separately deployable ingestion service. Follow the two initial Python issues and the term milestones. Do not interpret this teaching seed as a complete ingestion implementation.
