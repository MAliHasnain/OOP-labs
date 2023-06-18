class under_education(Exception):
    pass
def education():
    try:
        edu = int(input("Enter your years of education : "))
        if edu > 16:
            print("You are elegible!! ")
        else:
            raise under_education()
    except ValueError:
        print("Invalid value! ")
    except under_education:
        print("You are not elligible!!")
education()
