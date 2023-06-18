class point:
    def __init__(self,x,y):
        self.x = int(input("Enter X :"))
        self.y = int(input("Enter Y : "))
    def __add__(self, p2):
        return f"{self.x + p2.x},{self.y + p2.y}"
    def __lt__(self,p2):
        a = self.x < p2.x
        b = self.y < p2.y
        if a and b :
            return "True. P1 is smaller than P2"
        else:
            return "False P1 is not smaller than P2"
    def __gt__(self, p2):
        a = self.x > p2.x
        b = self.y > p2.y
        if a and b:
            return "True. P1 is greater than P2"
        else:
            return "False. P1 is not greater than P2"
p1 = point(2,4)
p2 = point(4,5)
print(p1+p2)
print(p1.__lt__(p2))
print(p1.__gt__(p2))
