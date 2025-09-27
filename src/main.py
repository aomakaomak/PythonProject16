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


class Category:
    name:str
    description: str
    products: list[str]

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)



cat1 = Category("Food", "Some", ["Banana", "Cheese"])
cat2 = Category("Drinks", "Some", ["Water", "Vodka"])

print(Category.number_of_categories)
print(Category.number_of_products)


