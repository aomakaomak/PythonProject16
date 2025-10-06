from src.base_category import BaseCategory


class Order(BaseCategory):

    def __init__(self, link, price, quantity):
        if quantity < 1:
            raise ValueError("Количество должно быть >= 1")
        self.link = link
        self.quantity = quantity
        self.price = price
        self.amount = self.quantity * self.price

    def __str__(self):
        return f"Куплен товар {self.link} в количестве {self.quantity} на общую сумму {self.amount}."

    orders = []

    def add_product(self):

        order_n = [self.link, self.quantity, self.amount]
        self.orders.append(order_n)
        # print(str(self))
        return self.orders


# order1 = Order("link1", 10, 1)
# order2 = Order("link2", 20, 1)
# print(order)

# orders = order1.add_product()
# print(orders)
#
# orders = order2.add_product()
# print(orders)
