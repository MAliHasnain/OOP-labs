# class A:
#     def func(self):
#         print("Class A")
# class B:
#     def func(self):
#         print("class B")
# class C(A,B):
#     def func(self):
#         print("class C")
# class D(C,B):
#     def func(self):
#         print("class D")
# obj=D()
# print(D.mro())

class A:
    def func(self):
        print("class A")
class B(A):
    def func(self):
        print("class B")
class C(A,B):
    def func(self):
        print("class C")
obj1 = C()
print(C.mro())

