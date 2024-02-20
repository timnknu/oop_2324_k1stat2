# негарний варіант класа
class QuadraticEquation:
    def solve_q_equation(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D < 0:
            print('No solutions')
            return
        x1 = (-self.b + D ** 0.5) / (2 * self.a)
        x2 = (-self.b - D ** 0.5) / (2 * self.a)
        print(x1, x2)

eq1 = QuadraticEquation()
eq1.a = 1.0
eq1.b = -2.0
eq1.c = 1.0

second_eq = QuadraticEquation()
second_eq.a = 1.0
second_eq.b = -2.0
second_eq.c = 0.0

eq1.solve_q_equation()

second_eq.solve_q_equation() # second_eq['solve'](second_eq)