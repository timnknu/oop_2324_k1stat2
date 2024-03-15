from linear_equation import Equation

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
