def calculate_total(price, quantity):
    return price * quantity


def calculate_discount(total):
    if total >= 50000:
        return total * 0.10
    elif total >= 25000:
        return total * 0.05
    else:
        return 0


products = [
    {"name": "Gold Ring", "price": 25000, "quantity": 1},
    {"name": "Gold Chain", "price": 50000, "quantity": 1},
    {"name": "Silver Ring", "price": 2000, "quantity": 2},
]

grand_total = 0

for product in products:
    total = calculate_total(
        product["price"],
        product["quantity"]
    )

    discount = calculate_discount(total)
    final_price = total - discount
    grand_total += final_price

    print(f"Product: {product['name']}")
    print(f"Total: ₹{total}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"Final Price: ₹{final_price:.2f}")
    print("-------------------")

print(f"Grand Total: ₹{grand_total:.2f}")