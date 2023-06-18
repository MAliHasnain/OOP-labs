class negative_Value(Exception):
    pass
def factorial():
    try:
        n = int(input("Enter te value for its factorial: "))
        if n == 1 :
            return 1
        elif n <= 0 :
            raise negative_Value
        else:
            print("The answer is : ",n*(n-1))
    except ValueError:
        print("There is a value erorr!!")
    except negative_Value :
        print("negative  value has no factorial!!")
factorial()