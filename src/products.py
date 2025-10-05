from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, product_data):
        product = cls(**product_data)
        return product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price >= self.__price:
            self.__price = new_price
        else:
            access = input("Подтвердите цену: y = да, n = нет: ")
            print(access)
            if access == "y":
                self.__price = new_price

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError(f"Ожидался Product, а получен {type(other).__name__}")
        elif type(self) is not type(other):
            raise TypeError("Это продукты разных классов")
        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.efficiency}', '{self.model}', {self.memory}, '{self.color}')"


class LawnGrass(Product):

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):

        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity}, '{self.country}', {self.germination_period}, '{self.color}')"


# if __name__ == "__main__":
#     dictionary1 = {
#         "name": "Cucumber",
#         "description": "Very tasty",
#         "price": 10.5,
#         "quantity": 10,
#         "efficiency": 20,
#         "model": "Samsung",
#         "memory": 64,
#         "color": "white"
#
#     }
#     dictionary2 = {
#         "name": "Apple",
#         "description": "Very tasty",
#         "price": 233.5,
#         "quantity": 30,
#         "efficiency": 30,
#         "model": "Xiaomi",
#         "memory": 32,
#         "color": "black"
#     }
#     dictionary3 = {
#         "name": "Orange",
#         "description": "Very tasty",
#         "price": 213.5,
#         "quantity": 120,
#         "country": "China",
#         "germination_period": 1,
#         "color": "green"
#     }
#     dictionary4 = {
#         "name": "Cucumber",
#         "description": "Very tasty",
#         "price": 2345.5,
#         "quantity": 10,
#         "country": "China",
#         "germination_period": 3,
#         "color": "blue"
#     }
#
#     product1 = Smartphone.new_product(dictionary1)
#     product2 = Smartphone.new_product(dictionary2)
#     product3 = LawnGrass.new_product(dictionary3)
#     product4 = LawnGrass.new_product(dictionary4)
#
#     print(product1)
#     print(product2)
#     print(product3)
#     print(product4)
#
#     print(product1 + product2)
#     print(product3 + product4)
#
#     print(product1 + product4)
#     print(product3 + product2)


#     #
#     #     product_list = []
#
#     product1 = Product.new_product(dictionary1)
#     product2 = Product.new_product(dictionary2)
#     product3 = Product.new_product(dictionary3)
#     product4 = Product.new_product(dictionary4)
# #
#     print(product1)
#     print(product2)
#     print(product3)
#     print(product4)
# #
#     product_wrong = "Banana"
#
#     print(product1 + product2)
# print(product1 + product_wrong)

# print(product1.name)
#     print(type(product1))
#
# print(product1.name)
# print(product1.description)
# print(product1.price)
# print(product1.quantity)
#
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     print(product3.name)
#     print(product3.description)
#     print(product3.price)
#     print(product3.quantity)
#
#     print(product4.name)
#     print(product4.description)
#     print(product4.price)
#     print(product4.quantity)
#
#     print(product2.price)
#
#     product2.price = 0  # setter сработает → "Цена не должна быть нулевая или отрицательная"
#
#     product2.price = -10  # setter сработает → то же сообщение
#
#     print(product2.price)
#
#     product2.price = 200
#
#     print(product2.price)


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


#     def new_product(cls, dictionary, product_list):
#         for product in product_list:
#             if dictionary.get("name") == product.name:
#                 product.price = max(product.price, dictionary.get("price"))
#                 product.quantity += dictionary.get("quantity")
#                 return product
#         product = cls(
#             dictionary.get("name"),
#             dictionary.get("description"),
#             dictionary.get("price"),
#             dictionary.get("quantity"),
#         )
#         product_list.append(product)
#         return product
