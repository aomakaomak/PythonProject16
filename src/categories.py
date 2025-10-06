from src.base_category import BaseCategory
from src.products import Product


class Category(BaseCategory):
    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Вы добавляете не продукт")

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


class MyList:
    category: Category

    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        if self.i + 1 < len(self.category.products_in_list):
            self.i += 1
            return self.category.products_in_list[self.i]
        else:
            raise StopIteration


# if __name__ == "__main__":
#
#
#
#     product1 = Product("Cucumber", "Very tasty", 23.5, 10)
#     product2 = Product("Tomato", "Very fresh", 45.2, 20)
#     product3 = Product("Limonade", "Cool", 12.3, 30)
#     product4 = Product("Juice", "Natural", 29.2, 40)
#     product5 = Product("Vodka", "Natural", 229.2, 50)
#
#     product_smart = Smartphone(name="Samsung S20FE", description="local", price=700, quantity=10, efficiency="A", model="S20FE", memory=64, color="white")
#     product_lawn = LawnGrass(name="Grass", description="local", price=100, quantity=200, country="China", germination_period=2, color="green")
#
#     cat1 = Category("Food", "Some", [product1, product2])
#     cat2 = Category("Drinks", "Some", [product3, product4])
#     print(cat1)
#     print(cat2)
#     print(cat1.products)
#     print(cat2.products)
#
#     cat2.add_product(product_smart)
#     print(product5.name)
#
#     print(cat2.products)
#
#     print(Category.category_count)
#     print(Category.product_count)
#
#     print(cat1)
#     print(cat2)
# #
#     category = MyList(cat1)
#
#     for product in category:
#         print(product)


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

# print(cat1.category_count)
# print(cat1.product_count)

# print(cat1.__products)
