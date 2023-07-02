# from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "name fidelity")

class LineItme:
    def __init__(self, product, quantity, price) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price
    def total(self):
        return self.quantity * self.price

class Order:
    def __init__(self, customer, cart, promotion=None) -> None:
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
    
    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    def due(self):
        if self.promotion == None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount
    def __repr__(self) -> str:
        return "<Order total: {:.2f} due: {:.2f}>".format(self.total(), self.due())


def FidelityPromo(order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0
    

def BulkItemPromo(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1           
    return discount
    
def LargeOrderPromo(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

if __name__ == "__main__":
    joe = Customer("John Doe", 0)
    ann = Customer("Ann Smith", 1500)
    cart = [LineItme("banana", 4, .5), LineItme("apple", 10, 1.5), LineItme("watermellon", 5, 5.0)]
    print(Order(ann, cart, FidelityPromo))
    print("Hello World")
    