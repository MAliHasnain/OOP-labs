from abc import ABCMeta,abstractmethod
class Animal (metaclass = ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def talk(self):
        pass
class Cat(Animal):
    def talk(self):
        print(f'The cat {self.name} talks as "Meao meo".')
class Dog(Animal):
    def talk(self):
        print(f'The dog {self.name} barks as "waof waof".')
cat1 = Cat("Mano")
cat1.talk()
dog1 = Dog("Tonny")
dog1.talk()