class point:
    def __init__(self,x,y):
        self.x = int(input("Enter X :"))
        self.y = int(input("Enter Y : "))
    def __add__(self, p2):
        return f"{self.x + p2.x},{self.y + p2.y}"
p1 = point(2,4)
p2 = point(2,4)
print(p1+p2)
