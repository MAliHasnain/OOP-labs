from abc import ABCMeta,abstractmethod
class Person(metaclass = ABCMeta):
    def __init__(self,price):
        self.price = price
    @abstractmethod
    def ticket_price(self):
        pass
class  Employed_Person(Person):
    def ticket_price(self):
        print("The orignal price for Employed person is: ", self.price)
        concession = (0.8 * self.price)
        print("The ticket price after concession is : ",concession)
class  Student(Person):
    def ticket_price(self):
        print("The orignal price for Student  is: ", self.price)
        concession = (0.5 * self.price)
        print("The ticket price after concession is : ",concession)
A = Employed_Person(1000)
A.ticket_price()
print()
B = Student(800)
B.ticket_price()
