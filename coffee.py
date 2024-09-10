


class Coffee:
    coffees = []

    def __init__(self, name):
        if isinstance(name, str) and len(name) >= 3:
            self._name = name
            Coffee.coffees.append(self)
        else:
            raise ValueError("Coffee name must be at least 3 characters long")

    @property
    def name(self):
        return self._name

    def orders(self):
        from order import Order
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        total_price = sum([order.price for order in self.orders()])
        num_orders = self.num_orders()
        return total_price / num_orders if num_orders > 0 else 0

    