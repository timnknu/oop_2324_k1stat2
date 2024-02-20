class QuadraticEquation:
    def __init__(self, coef_a, coef_b = None, coef_c = None):
        if isinstance(coef_a, QuadraticEquation):
            print("We're taking data from existing object")
            self.a = coef_a.a
            self.b = coef_a.b
            self.c = coef_a.c
        else:
            print("We're operating on numbers")
            self.a = coef_a
            self.b = coef_b
            self.c = coef_c

    def solve_q_equation(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D < 0:
            # розв'язків немає
            return []
        if abs(D) < 1e-10: # щоб уникнути похибок заокруглення
            # розв'язок один
            return [ -self.b  / (2 * self.a) ]
        # else:
        # розв'язків два
        x1 = (-self.b + D ** 0.5) / (2 * self.a)
        x2 = (-self.b - D ** 0.5) / (2 * self.a)
        return [x1, x2]

eq1 = QuadraticEquation(1.0, -2.0, 1.0)

second_eq = QuadraticEquation(eq1)  # конструктро копіювання має взяти всі дані з eq1
#
sol1 = eq1.solve_q_equation()
second_sol = second_eq.solve_q_equation()

print(sol1, second_sol)
