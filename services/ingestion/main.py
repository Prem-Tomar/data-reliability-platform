"""Day-one learning seed for the future ingestion service.

Run from the repository root: python services/ingestion/main.py
This uses synthetic values only. It is not a production service.
"""

order_id = "ORDER-001"
quantity = 2
unit_price_paise = 12500
order_total_paise = quantity * unit_price_paise

print("Order:", order_id)
print("Quantity:", quantity)
print("Total (paise):", order_total_paise)
