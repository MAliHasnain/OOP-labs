def smart_division():
    try:
        num = int(input("Enter the numerator : "))
        den = int(input('Enter the denomenator : '))
        print("The answer is : ", num / den)
    except ValueError:
        print("There is a value error!!")
    except ZeroDivisionError:
        print("Denomenator should not be zero!!")
smart_division()