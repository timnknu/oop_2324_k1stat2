from linear_equation import Equation
from quadr_equation import QuadraticEquation


if __name__ == "__main__":
    e = QuadraticEquation(1.0, -2.0, -4)
    r = e.solve()
    print(r)
