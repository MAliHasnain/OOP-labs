def decorator_x(func):
    def wrapper():
        print_x()
        func()
        print_x()
    return wrapper
def decorator_y(func):
    def wrapper():
        print_y()
        func()
        print_y()
    return wrapper
def print_x():
    print("X"*5)
def print_y():
    print("Y"*5)
@decorator_x
@decorator_y
def printhello():
    print("Hello world")
printhello()
