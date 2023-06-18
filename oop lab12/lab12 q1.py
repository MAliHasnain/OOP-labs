class Complex_Number:
    def __init__(self):
        self.x = str(input("Enter X = "))
        self.y = str(input("Enter Y = "))
    def __str__(self):
        return self.x+"i" + "+" + self.y+"j"
q1= Complex_Number()
print(q1)
