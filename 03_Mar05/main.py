class Equation:
    INF_SOLS = (None, None, None, None, None)
    NO_SOLS = tuple()

    def __init__(self, b, c):
        self._b = b
        self._c = c
    def solve(self):
        # bx + c =  0 => x = -c/b
        if self._b==0:
            if self._c==0:
                return Equation.INF_SOLS
            else:
                return Equation.NO_SOLS
        else:
            return (- self._c / self._b, ) # кортеж з одного елемента

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self._a = a
        super().__init__(b, c)
    #
    def solve(self):
        if self._a == 0:
            return super().solve()
        else:
            D = self._b ** 2 - 4 * self._a * self._c
            if D < 0:  # розв'язків немає
                return Equation.NO_SOLS
            if abs(D) < 1e-10:  # щоб уникнути похибок заокруглення
                # розв'язок один
                return (-self._b / (2 * self._a), )
            else:
                # розв'язків два
                x1 = (-self._b + D ** 0.5) / (2 * self._a)
                x2 = (-self._b - D ** 0.5) / (2 * self._a)
                return (x1, x2)
    #


if __name__ == "__main__":
    e = QuadraticEquation(1.0, -2.0, -4)
    r = e.solve()
    print(r)



    # e = Equation(1.0, 2.0)
    # r = e.solve()
    # assert r==(-2.0/1.0, )
    #
    # e = Equation(0.0, 2.0)
    # r = e.solve()
    # assert r==Equation.NO_SOLS
    #
    # e = Equation(0.0, 0.0)
    # r = e.solve()
    # assert r==Equation.INF_SOLS
