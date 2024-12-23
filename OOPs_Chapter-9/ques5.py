class Order:
    def __init__(self, items, price):
        self.items = items
        self.price = price

    def __gt__(self, o2):
        return self.price > o2.price

o1 = Order("chips", 20)
o2 = Order("kurkure", 15)

print(o1>o2)