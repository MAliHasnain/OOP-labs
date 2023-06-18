class Circle:
    def __init__(self,r):
        self.r = int(input("Enter radius :"))
    def __lt__(self,c2):
        a = self.r < c2
        if a:
            return "C1 is smaller than C2"
        else:
            return "C2 is smaller than C1"
    def __gt__(self, c2):
        a = c2 > self.r
        if a:
            return "C2 is greater than C1"
        else:
            return "C1 is greater than C2"
c1 = Circle(2)
c2 = Circle(4)
print(c1.__lt__(c2))
print(c1.__gt__(c2))
