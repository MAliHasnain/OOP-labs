from abc import ABCMeta, abstractmethod
class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass
class Sub(Super):
    def action(self):
        print("Your are in sub class!!! ")
X=Sub()
X.action()