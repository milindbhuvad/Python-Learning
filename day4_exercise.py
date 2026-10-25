class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Email: {self.email}")

customer1 = Customer("John Doe", "john.doe@example.com")
customer1.display_details()

customer2 = Customer("Jane Smith", "jane.smith@example.com")
customer2.display_details()