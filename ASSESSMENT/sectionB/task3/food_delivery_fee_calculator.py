from functools import reduce

records = [
    {"id": 1, "name": "Pizza Hut", "amount": 400},
    {"id": 2, "name": "Dominos", "amount": 800},
    {"id": 3, "name": "KFC", "amount": 1200},
    {"id": 4, "name": "Swiggy", "amount": 1600},
    {"id": 5, "name": "Zomato", "amount": 2200},
    {"id": 6, "name": "Burger King", "amount": 3000}
]

def calculate_fee(record):
    amount = record["amount"]

    if amount <= 500:
        return amount * 0.05
    elif amount <= 1500:
        return amount * 0.08
    else:
        return amount * 0.10


updated_records = list(
    map(lambda record: {**record, "fee": calculate_fee(record)}, records)
)    

threshold = 100

high_fee_records = list(
    filter(lambda record: record["fee"] > threshold, updated_records)
)

print("\n===== AUDIT: FEES ABOVE ₹100 =====")

for record in high_fee_records:
    print(record)

total_fee = reduce(
    lambda total, record: total + record["fee"],
    updated_records,
    0
)

print("\nTotal fee across all records: ₹{:.2f}".format(total_fee))    