class Complex_Number:
    def __init__(self):
        self.x = str(input("Enter X = "))
        self.y = str(input("Enter Y = "))
    def __str__(self):
        return "("+self.x+","+ self.y+ ")"
q2= Complex_Number()
print(q2)
