import pytest
from order import Order
from customer import Customer
from coffee import Coffee

def test_order_initialization():
    customer = Customer("Tom")
    coffee = Coffee("Mocha")

    # Valid Order
    order = Order(customer, coffee, 5.0)
    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0

    # Invalid price
    with pytest.raises(ValueError):
        Order(customer, coffee, 0.5)  # Less than 1.0

    with pytest.raises(ValueError):
        Order(customer, coffee, 15.0)  # Greater than 10.0

    # Invalid customer
    with pytest.raises(ValueError):
        Order("Invalid Customer", coffee, 5.0)

    # Invalid coffee
    with pytest.raises(ValueError):
        Order(customer, "Invalid Coffee", 5.0)
