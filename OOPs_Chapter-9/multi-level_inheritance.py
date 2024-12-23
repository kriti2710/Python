class Car():
    @staticmethod
    def start():
        print("car started")
    
    def stop():
        print("car stopped")
    
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Petrol")
car1.start()