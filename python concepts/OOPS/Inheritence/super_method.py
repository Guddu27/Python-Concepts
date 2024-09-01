


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class KiaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()


car1 = KiaCar("Seltos", "Electric")
print(car1.type)