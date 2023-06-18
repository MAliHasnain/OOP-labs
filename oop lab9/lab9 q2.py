def Division_decorator(func):

    def divisor(num,den):
        if den == 0 :
            print("Divison by 0 is not possible!!!")
        else:
            func(num,den)

    return divisor
@Division_decorator
def division(num,den):
    print(int(num/den))
division(15,0)


