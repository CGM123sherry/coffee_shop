Coffee_shop
A python application that consist of three main entities: `Customer`, `Coffee`, and `Order`. The relationships are as follows:

- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- An `Order` belongs to one `Customer` and one `Coffee`.

The `Customer` and `Coffee` entities have a many-to-many relationship through the `Order` entity.

## Classes

### `Customer`

- **Attributes**:
- `name`: The name of the customer.
- **Methods**:
- `create_order(coffee, price)`: Creates a new order for the customer with the given coffee and price.

### `Coffee`

- **Attributes**:
- `name`: The name of the coffee.
- **Methods**:
- `num_orders()`: Returns the total number of orders for this coffee.
- `average_price()`: Returns the average price for all orders of this coffee.

### `Order`

- **Attributes**:
- `customer`: The customer who placed the order.
- `coffee`: The coffee being ordered.
- `price`: The price of the order.
- **Class Attribute**:
- `orders`: A list containing all orders created in the system.

### Setup and Preparation

- fork and clone the repo

# https://github.com/CGM123sherry/coffee_shop

- Set up a virtual environment within this directory using `pipenv`:
  ```bash
  pipenv install
  pipenv shell
  ```
- Install any necessary packages, such as `pytest` for testing:
  ```bash
  pipenv install pytest
  ```
