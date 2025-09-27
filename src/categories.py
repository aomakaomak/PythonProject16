from products import Product

class Category:
    name:str
    description: str
    product_list: list[str]

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, product_list=None):
        self.name = name
        self.description = description
        self.product_list = product_list if product_list else []

        Category.number_of_categories += 1
        Category.number_of_products += len(product_list) if product_list else 0


if __name__ == "__main__":
    product1 = Product("Cucumber", "Very tasty", 23.5, 10)
    product2 = Product("Tomato", "Very fresh", 45.2, 20)
    product3 = Product("Limonade", "Cool", 12.3, 30)
    product4 = Product("Juice", "Natural", 29.2, 40)

    cat1 = Category("Food", "Some", [product1, product2])
    cat2 = Category("Drinks", "Some", [product3, product4])

    print(Category.number_of_categories)
    print(Category.number_of_products)
    print(list(cat1.product_list))
    print(list(cat2.product_list))

    print(cat1.number_of_categories)
    print(cat1.number_of_products)











