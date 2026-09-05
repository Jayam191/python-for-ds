
import requests
import json
import os

# --------------------------------------------------
# 1. Fetch first 5 records from API
# --------------------------------------------------

url = "https://jsonplaceholder.typicode.com/posts?_limit=5"

try:
    response = requests.get(url)

    # Check HTTP status code before calling .json()
    if response.status_code != 200:
        print(f"API Error: Unable to fetch records. Status code: {response.status_code}")
        exit()

    restaurants = response.json()

    print("Mock Restaurants:")
    for restaurant in restaurants:
        print(f"ID: {restaurant['id']}, Title: {restaurant['title']}")

    # --------------------------------------------------
    # 2. Calculate commission for 6 orders
    # --------------------------------------------------

    order_amounts = [150, 200, 250, 450, 600, 1000]

    # Tiered commission using map() and lambda
    commissions = list(
        map(
            lambda amount: amount * 0.10 if amount <= 200
            else amount * 0.15 if amount <= 500
            else amount * 0.20,
            order_amounts
        )
    )

    print("\nOrder Commissions:")

    for amount, commission in zip(order_amounts, commissions):
        print(f"Order Amount: ₹{amount}, Commission: ₹{commission:.2f}")

    # --------------------------------------------------
    # 3. Save fetched records to JSON file
    # --------------------------------------------------

    file_path = "data/processed/records.json"

    # Create folder if it does not exist
    os.makedirs("data/processed", exist_ok=True)

    with open(file_path, "w") as file:
        json.dump(restaurants, file, indent=2)

    print(f"\nRecords saved successfully to {file_path}")

except requests.exceptions.RequestException as e:
    print(f"API request failed: {e}")

except (KeyError, ValueError) as e:
    print(f"Error while processing API data: {e}")

except OSError as e:
    print(f"File error: {e}")
