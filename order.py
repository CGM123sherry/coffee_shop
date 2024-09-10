# from coffee import Coffee
# from customer import Customer


class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if isinstance(customer, Customer) and isinstance(coffee, Coffee) and 1.0 <= price <= 10.0:
            self._customer = customer
            self._coffee = coffee
            self._price = price
            Order.orders.append(self)
        else:
            raise ValueError("Invalid Order parameters")

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
