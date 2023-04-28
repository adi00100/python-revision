class A:
    def print(self):
            print("This is from class A")

class B(A):
    def print(self):
            print("This is from class B")

class C(B):
    def print(self):
            print("This is from class C")

class D(C):
    def print(self):
            print("This is from class D")

class E(D):
    def print(self):
            print("This is from class E")
            super(D,self).print()

print("MRO of E",E.mro())
E().print()