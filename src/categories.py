from products import Product


class Category:
    name: str
    description: str
    __products: list

    number_of_categories = 0
    number_of_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.number_of_categories += 1
        Category.number_of_products += len(products) if products else 0

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.number_of_products += 1


    @property
    def products(self):
        product_list = []
        for product in self.__products:
            string = str(product)
            product_list.append(string)
        result = "\n".join(product_list)
        return result

    @property
    # создаем геттер, чтобы посчитать количество товаров в категории
    def products_in_list(self):
        return self.__products

    def __str__(self):
        goods_count = 0
        for product in self.__products:
            goods_count += product.quantity
        return f"{self.name}, количество продуктов: {goods_count} шт."



if __name__ == "__main__":

    product1 = Product("Cucumber", "Very tasty", 23.5, 10)
    product2 = Product("Tomato", "Very fresh", 45.2, 20)
    product3 = Product("Limonade", "Cool", 12.3, 30)
    product4 = Product("Juice", "Natural", 29.2, 40)
    product5 = Product("Vodka", "Natural", 229.2, 50)

    cat1 = Category("Food", "Some", [product1, product2])
    cat2 = Category("Drinks", "Some", [product3, product4])
    print(cat1)
    print(cat2)
    print(cat1.products)
    print(cat2.products)

    cat2.add_product(product5)
    print(product5.name)

    print(cat2.products)

    print(Category.number_of_categories)
    print(Category.number_of_products)

    print(cat1)
    print(cat2)



# prod1 = Category.add_product(product1)
# prod2 = Category.add_product(product2)
# prod3 = Category.add_product(product3)
# prod4 = Category.add_product(product4)
# print(prod1)
# print(type(prod1))

# print(product1.name)
# print(product1.description)
# print(product1.price)
# print(product1.quantity)
#
# print(product4.name)
# print(product4.description)
# print(product4.price)
# print(product4.quantity)

# cat1 = Category("Food", "Some", [prod1, prod2])
# cat2 = Category("Drinks", "Some", [prod3, prod4])


# print(list(cat1.product_list))
# print(list(cat2.product_list))

# print(cat1.number_of_categories)
# print(cat1.number_of_products)

# print(cat1.__products)
