import random
from collections import deque

class Customer:
    def __init__(self, customer_id, items):
        self.customer_id = customer_id
        self.items = items

    def __str__(self):
        return f"Customer {self.customer_id} ({self.items} items)"


class CheckoutLine:
    def __init__(self):
        self.queue = deque()
        self.checkout_time = 0  # Time until the next customer is served

    def add_customer(self, customer):
        self.queue.append(customer)
        print(f"Customer added to queue: {customer}")

    def serve_next_customer(self):
        if not self.queue:
            print("Checkout line is empty.")
            return

        customer = self.queue.popleft()
        service_time = customer.items * 2  # Simulate service time (2 seconds per item)
        self.checkout_time += service_time
        print(f"Serving {customer}. Service time: {service_time} seconds.")
        print(f"Next customer will be served at {self.checkout_time} seconds.")


# Simulate customer arrivals and service
checkout = CheckoutLine()

for i in range(1, 6):  # Simulate 5 customers
    num_items = random.randint(1, 10)  # Random number of items
    customer = Customer(i, num_items)
    checkout.add_customer(customer)

# Serve customers
for _ in range(5):  # Serve all 5 customers
    checkout.serve_next_customer()