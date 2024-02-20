class QuadraticEquation:
    def __init__(self, coef_a, coef_b, coef_c):
        self.a = coef_a
        self.b = coef_b
        self.c = coef_c

    def solve_q_equation(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D < 0:
            print('No solutions')
            return
        x1 = (-self.b + D ** 0.5) / (2 * self.a)
        x2 = (-self.b - D ** 0.5) / (2 * self.a)
        print(x1, x2)

eq1 = QuadraticEquation(1.0, -2.0, 1.0)

second_eq = QuadraticEquation(1.0, -2.0, 0.0)

eq1.solve_q_equation()
second_eq.solve_q_equation()