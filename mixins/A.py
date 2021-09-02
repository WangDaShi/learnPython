class A:
    total = 123

class B(A):
    pass

class C(A):
    pass

# our code 
class M:
    total = 0
    def print_total(self):
        print(self.total)

class D(B,M):
    pass

class E(C,M):
    pass

e = E()

e.print_total()
# print(e.min)
