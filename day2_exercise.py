products = [
    {
        "name": "Gold Ring",
        "price": 25000
    },
    {
        "name": "Gold Chain",
        "price": 50000
    },
    {
        "name": "Diamond Ring",
        "price": 75000
    }
]

for product in products:
    print(f"Product: {product['name']}")
    print(f"Price: ₹{product['price']}")
    print("------------------------------------")