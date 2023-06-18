import abc
class Calculator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self,val1,val2):
        self.val1 = int(input("Enter the first value: "))
        self.val2 = int(input("Enter the second value: "))
    def Mathematical_Operation(self):
        pass
class Addition_operation(Calculator):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print("The sum of numbers are:",self.val1 + self.val2)
class Substraction_operation(Calculator):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print("The difference of numbers is : ",self.val1-self.val2)
class Multiplication_operation(Calculator):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print("The product of numbers is : ",self.val1*self.val2)
class Division_operation(Calculator):
    def __init__(self,val1,val2):
        super().__init__(val1,val2)
    def Mathematical_Operation(self):
        super().Mathematical_Operation()
        print("The divident of numbers is : ",self.val1/self.val2)
A = Addition_operation(5,4)
A.Mathematical_Operation()
B = Substraction_operation(5,4)
B.Mathematical_Operation()
C = Multiplication_operation(5,4)
C.Mathematical_Operation()
D = Division_operation(5,4)
D.Mathematical_Operation()
