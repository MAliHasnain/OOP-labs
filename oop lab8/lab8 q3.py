import abc
class Vehicle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self,model):
        self.model = model
    def PrintDetails(self):
        pass
class Car(Vehicle):
    def __init__(self,model,sunroof,capacity):
        super().__init__(model)
        self.sunroof = sunroof
        self.capacity = capacity
    def PrintDetails(self):
        super().PrintDetails()
        print(f"The model is{self.model}\nThe sunroof is {self.sunroof}\nThe capacity is {self.capacity}")
class Truck(Vehicle):
    def __init__(self,model,bulletproof,netweight):
        super().__init__(model)
        self.bulletproof = bulletproof
        self.netweight = netweight
    def PrintDetails(self):
        super().PrintDetails()
        print(f"The bullet proof is {self.bulletproof}\nThe netweight of truck is {self.netweight} ")
class Motorcycle(Vehicle):
    def __init__(self,model,brand,speed):
        super().__init__(model)
        self.brand = brand
        self.speed =speed
    def PrintDetails(self):
        super().PrintDetails()
        print(f"The model of motorcycle is {self.model}\nThe brand of motorcycle is {self.brand}\nThe speed of motorcycle is {self.speed} ")
Unique = Motorcycle("2019","Super Star","70")
Unique.PrintDetails()
