import requests
import json

class Order:
    def __init__(self, order_id, name, amount, status):
        self.order_id = order_id
        self.name = name
        self.amount = amount
        self.status = status

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "name": self.name,
            "amount": self.amount,
            "status": self.status
        }

    def __str__(self):
        return (
            f"ID: {self.order_id} | "
            f"Restaurant: {self.name} | "
            f"Amount: ₹{self.amount:.2f} | "
            f"Status: {self.status}"
        )            

def fetch_restaurants():
    url = "https://jsonplaceholder.typicode.com/posts?_limit=10"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print("\n===== TOP 10 RESTAURANTS =====")

            orders = []

            for item in data:
                order = Order(
                    item["id"],
                    item["title"],
                    0.0,
                    False
                )

                orders.append(order)
                print(order)

            return orders

        else:
            print("API error. Status code:", response.status_code)
            return []

    except Exception as e:
        print("API request failed:", e)
        return []    


def calculate_commission(order):
    if order.amount <= 500:
        return order.amount * 0.05
    elif order.amount <= 1500:
        return order.amount * 0.08
    else:
        return order.amount * 0.10

def save_records(records, filepath):
    try:
        data = [record.to_dict() for record in records]

        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)

        print("Records saved successfully.")

    except Exception as e:
        print("Error while saving records:", e)

    finally:
        print("Save operation complete")


def load_records(filepath):
    try:
        with open(filepath, "r") as file:
            data = json.load(file)

        records = [
            Order(
                item["order_id"],
                item["name"],
                item["amount"],
                item["status"]
            )
            for item in data
        ]

        print("Records loaded successfully.")
        return records

    except FileNotFoundError:
        print("File not found. Returning an empty list.")
        return []

    except Exception as e:
        print("Error while loading records:", e)
        return []

    finally:
        print("Load operation complete")
    
def main():
    orders = []

    while True:
        print("\n===== FOOD DELIVERY LIVE DATA PIPELINE =====")
        print("1. Fetch and display restaurants")
        print("2. Add a new restaurant")
        print("3. Calculate commission")
        print("4. Save and load records")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            orders = fetch_restaurants()



        elif choice == "2":
            name = input("Enter restaurant name: ")

            while True:
                amount = input("Enter order amount: ")

                try:
                    amount = float(amount)
                    break
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            status = input("Is the order delivered? (yes/no): ").lower()

            if status == "yes":
                status = True
            else:
                status = False

            order_id = len(orders) + 1

            order = Order(order_id, name, amount, status)
            orders.append(order)

            print("Restaurant added successfully.")
            print(order)




        elif choice == "3":
            commissions = list(
                map(lambda order: calculate_commission(order), orders)
            )

            print("\n===== COMMISSION FOR ALL RECORDS =====")

            for order, commission in zip(orders, commissions):
                print(f"{order.name}: ₹{commission:.2f}")

            high_commission_orders = list(
                filter(
                    lambda order: calculate_commission(order) > 100,
                    orders
                )
            )

            print("\n===== AUDIT: COMMISSION ABOVE ₹100 =====")

            for order in high_commission_orders:
                print(order)




            
        elif choice == "4":
            filepath = "ASSESSMENT/sectionC/mini-capstone/data/processed/records.json"

            save_records(orders, filepath)

            loaded_orders = load_records(filepath)

            orders = loaded_orders

            print("\n===== LOADED RECORDS =====")

            for order in orders:
                print(order)

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter 1 to 5.")


if __name__ == "__main__":
    main()    