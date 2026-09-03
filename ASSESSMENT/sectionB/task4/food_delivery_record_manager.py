import json


class Order:
    def __init__(self, order_id, restaurant_name, amount, delivery_time_minutes, is_delivered):
        self.order_id = order_id
        self.restaurant_name = restaurant_name
        self.amount = amount
        self.delivery_time_minutes = delivery_time_minutes
        self.is_delivered = is_delivered


    def to_dict(self):
        return {
            "order_id": self.order_id,
            "restaurant_name": self.restaurant_name,
            "amount": self.amount,
            "delivery_time_minutes": self.delivery_time_minutes,
            "is_delivered": self.is_delivered
        }        

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["order_id"],
            data["restaurant_name"],
            data["amount"],
            data["delivery_time_minutes"],
            data["is_delivered"]
        )    


def save_records(records, filepath):
    try:
        data = [record.to_dict() for record in records]

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        print("Records saved successfully.")

    except Exception as e:
        print("Error while saving records:", e)

    finally:
        print("Operation complete") 

def load_records(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        records = [Order.from_dict(item) for item in data]

        print("Records loaded successfully.")
        return records

    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []

    except Exception as e:
        print("Error while loading records:", e)
        return []

    finally:
        print("Operation complete")

orders = [
    Order(1, "Pizza Hut", 500.0, 30, True),
    Order(2, "Dominos", 800.0, 40, True),
    Order(3, "KFC", 1200.0, 50, False)
]

filepath = "ASSESSMENT/sectionB/task1/food-delivery-pipeline/data/processed/missing.json"

save_records(orders, filepath)

loaded_orders = load_records(filepath)

print("\nLoaded orders:")

for order in loaded_orders:
    print(order.to_dict())
                   