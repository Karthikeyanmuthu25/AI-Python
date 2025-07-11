# ShoppingBill.py
# This script calculates the total cost of 3 items including a tax percentage.

def calculate_total_with_tax(prices, tax_percent):
    subtotal = sum(prices)
    tax_amount = subtotal * (tax_percent / 100)
    total = subtotal + tax_amount
    return subtotal, tax_amount, total

# Step 1: Get item prices
try:
    item1 = float(input("Enter price of Item 1: ₹"))
    item2 = float(input("Enter price of Item 2: ₹"))
    item3 = float(input("Enter price of Item 3: ₹"))

    prices = [item1, item2, item3]

    # Step 2: Get tax percentage
    tax_percent = float(input("Enter tax percentage (e.g. 5 for 5%): "))

    # Step 3: Calculate bill
    subtotal, tax_amount, total = calculate_total_with_tax(prices, tax_percent)

    # Step 4: Display results
    print("\n🧾 --- Bill Summary ---")
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Tax @ {tax_percent}%: ₹{tax_amount:.2f}")
    print(f"Total Bill: ₹{total:.2f}")

except ValueError:
    print("❌ Please enter valid numbers for prices and tax!")
