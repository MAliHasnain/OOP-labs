try:
    edu = int(input("Enter your years of education : "))
    if edu > 16 :
        print("You are elegible!! ")
    else :
        print("You are not eleible!!")
except ValueError:
    print("Invalid value! ")
