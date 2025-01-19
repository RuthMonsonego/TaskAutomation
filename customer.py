class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

# List of customers
customers = [
    Customer(1, "Yossi", "rut65756@gmail.com"),
    Customer(2, "Dani", "rut65756@gmail.com"),
    Customer(3, "Sarah", "rut65756@gmail.com"),
]

# Function that returns the customer by customer ID
def get_customer_by_id(customer_id):
    for customer in customers:
        if customer.customer_id == customer_id:
            return customer
    return None  # If no customer is found with this ID