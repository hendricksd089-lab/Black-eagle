menu = ["Coffee", "Tea", "Sandwich", "Cake"]

stock = {
    "Coffee": 50,
    "Tea": 40,
    "Sandwich": 15,
    "Cake": 10
}

price = {
    "Coffee": 2.50,
    "Tea": 2.00,
    "Sandwich": 5.50,
    "Cake": 4.00
}

total_stock_worth = 0.0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

print(f"The total value of stock in the cafe is: ${total_stock_worth:.2f}")