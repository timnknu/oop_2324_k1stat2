class Equation:
    INF_SOLS = -1
    def __init__(self, b, c):
        self._b = b
        self._c = c
    def solve(self):
        # bx + c =  0 => x = -c/b
        #(None, None, None, None, None)
        pass

print(Equation.INF_SOLS) # доступ до статичного поля (через ім'я класу)

e = Equation(1.0, 2.0)
print(e.INF_SOLS) # доступ до статичного поля (через об'єкт) -- краще не робити так