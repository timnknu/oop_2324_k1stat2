from linear_equation import Equation
from quadr_equation import QuadraticEquation

class BiQuadraticEquation(QuadraticEquation):
    def solve(self):
        ses = super().solve()
        if ses == Equation.NO_SOLS:
            return Equation.NO_SOLS
        #
        if ses == Equation.INF_SOLS:
            return Equation.INF_SOLS
        #
        result = []
        for xsq in ses:
            if xsq >= 0:
                result.append(xsq**0.5)
                result.append(- xsq**0.5)
        #
        if len(result) == 0:
            return Equation.NO_SOLS
        #

        return tuple(result)

if __name__ == "__main__":
    e = BiQuadraticEquation(1.0, -3.0, 2) # (x**2 - 1)*(x**2 - 2)
    #e = BiQuadraticEquation(1.0, -2.0, -1)  # (x**2 + 1)*(x**2 - 2)
    #e = BiQuadraticEquation(1.0, 3.0, 2)  # (x**2 + 1)*(x**2 + 2)
    r = e.solve()
    print(r)
