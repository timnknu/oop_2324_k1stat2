class A:
    def p(self):
        print('hello')

class B(A):
    def q(self):
        print('W')

b = B()
print(isinstance(b, B))
print(isinstance(b, A))

print(type(b))
print(type(b) is B)
print(type(b) is A)

