class A(object):
    def innn(self):
        print("in a")
class B(object):
    def innn(self):
        print("in b")
class X(A, B):
    def innn(self):
        print("in x")
class Y(B, A):
    def innn(self):
        print("in y")
class Z(X, Y):
    def innn(self):
        print("in z")
obj=z()
obj.innn()
