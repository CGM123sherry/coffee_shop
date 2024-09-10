


class Customer:
    customers = []

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
            Customer.customers.append(self)
        else:
            raise ValueError("Name must be a string with 1 to 15 characters")

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        customer_spend = {}
        for order in Order.orders:
            if order.coffee == coffee:
                if order.customer in customer_spend:
                    customer_spend[order.customer] += order.price
                else:
                    customer_spend[order.customer] = order.price
        return max(customer_spend, key=customer_spend.get, default=None)

    