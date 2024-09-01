
#! Create a class Order which stores item & its price. Use Dunder function __gt__() to conver that : order1 > order2 if price of order1 is greater than price of order2. ***[__gt__() : Greater than Function]***

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, od2):
        return self.price > od2.price
    
    #? The __gt__() dunder function return either true or false values.


od1 = Order("Kurkure", 10)
od2 = Order("Tea", 15)
print(od1 > od2)