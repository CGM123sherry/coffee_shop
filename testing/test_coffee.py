import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def test_coffee_initialization():
    # Valid Coffee
    coffee = Coffee("Espresso")
    assert coffee.name == "Espresso"

    # Invalid Coffee name
    with pytest.raises(ValueError):
        Coffee("La")  # Less than 3 characters

def test_coffee_orders():
    coffee = Coffee("Latte")
    customer = Customer("Alice")
    order = customer.create_order(coffee, 5.0)

    assert order in coffee.orders()

def test_coffee_customers():
    coffee = Coffee("Cappuccino")
    customer1 = Customer("John")
    customer2 = Customer("Jane")

    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 5.0)

    assert customer1 in coffee.customers()
    assert customer2 in coffee.customers()

def test_coffee_num_orders():
    coffee = Coffee("Latte")
    customer = Customer("Doe")
    customer.create_order(coffee, 5.0)
    customer.create_order(coffee, 6.0)

    assert coffee.num_orders() == 2

def test_coffee_average_price():
    coffee = Coffee("Latte")
    customer = Customer("Smith")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 6.0)

    assert coffee.average_price() == 5.0
