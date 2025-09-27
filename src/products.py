class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# if __name__ == "__main__":
#     product1 = Product("Cucumber", "Very tasty", 23.5, 10)
#     product2 = Product("Tomato", "Very fresh", 45.2, 20)
#
#     print(product1.name)
#     print(product1.description)
#     print(product1.price)
#     print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
