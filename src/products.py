class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dictionary, product_list):
        for product in product_list:
            if dictionary.get("name") == product.name:
                product.price = max(product.price, dictionary.get("price"))
                product.quantity += dictionary.get("quantity")
                return product
        product = cls(
            dictionary.get("name"),
            dictionary.get("description"),
            dictionary.get("price"),
            dictionary.get("quantity"),
        )
        product_list.append(product)
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


# if __name__ == "__main__":
#     dictionary1 = {
#         "name": "Cucumber",
#         "description": "Very tasty",
#         "price": 10.5,
#         "quantity": 10
#     }
#     dictionary2 = {
#         "name": "Apple",
#         "description": "Very tasty",
#         "price": 233.5,
#         "quantity": 30
#     }
#     dictionary3 = {
#         "name": "Orange",
#         "description": "Very tasty",
#         "price": 213.5,
#         "quantity": 120
#     }
#     dictionary4 = {
#         "name": "Cucumber",
#         "description": "Very tasty",
#         "price": 2345.5,
#         "quantity": 10
#     }
#
#     product_list = []
#
#     product1 = Product.new_product(dictionary1, product_list)
#     product2 = Product.new_product(dictionary2, product_list)
#     product3 = Product.new_product(dictionary3, product_list)
#     product4 = Product.new_product(dictionary4, product_list)
#
#     print(product1)
#     print(type(product1))
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
