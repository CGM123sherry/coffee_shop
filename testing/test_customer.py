import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_initialization():
    # Valid Customer
    customer = Customer("John")
    assert customer.name == "John"

    # Invalid Customer name
    with pytest.raises(ValueError):
        Customer("A" * 16)  # More than 15 characters

    with pytest.raises(ValueError):
        Customer("")  # Less than 1 character

def test_customer_orders():
    customer = Customer("Jane")
    coffee = Coffee("Latte")
    order = customer.create_order(coffee, 5.0)

    assert order in customer.orders()

def test_customer_coffees():
    customer = Customer("Doe")
    coffee1 = Coffee("Latte")
    coffee2 = Coffee("Espresso")
    customer.create_order(coffee1, 5.0)
    customer.create_order(coffee2, 6.0)

    assert coffee1 in customer.coffees()
    assert coffee2 in customer.coffees()

def test_customer_most_aficionado():
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee = Coffee("Cappuccino")
    
    customer1.create_order(coffee, 5.0)
    customer2.create_order(coffee, 6.0)
    customer2.create_order(coffee, 4.0)

    # customer2 should be the most aficionado
    assert Customer.most_aficionado(coffee) == customer2
