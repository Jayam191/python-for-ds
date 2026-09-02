restaurants = [
    "  pizza hut  ",
    "DOMINOS",
    "  McDonald's ",
    "",
    "12345",
    " kfc ",
    "SwIgGy ",
    "  ZOMATO"
]

amounts = [
    "Rs 150",
    "200.50",
    "Rs 300",
    "250",
    "Rs 175.50",
    "400",
    "Rs 125",
    "350.75"
]

valid_count = 0
skipped_count = 0

for restaurant in restaurants:
    restaurant = restaurant.strip()

    if restaurant == "" or restaurant.isdigit():
        print("Skipped invalid entry:", restaurant)
        skipped_count += 1
        continue

    restaurant = restaurant.title()
    print("Valid restaurant:", restaurant)
    valid_count += 1

running_total = 0.0

for amount in amounts:
    amount = amount.replace("Rs ", "")
    amount = float(amount)
    running_total += amount

    print("\nAmount:", amount)
    print("Running total:", running_total) 

print("\n===== Food Delivery Cleaning Summary =====")
print("Total valid records :", valid_count)
print("Total skipped       :", skipped_count)
print("Running total amount: Rs", running_total)    