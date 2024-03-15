class A:
    def pr(self):
        print('A, pr')
        print(self.f())
    def f(self):
        return -1


class B(A):
    def f(self):
        return 128

obj = A()
obj.pr()

obj2 = B()
obj2.pr()