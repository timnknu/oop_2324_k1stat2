# негарний варіант класа
class QuadraticEquation:
    def set_data(self, coef_a, coef_b, coef_c):
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


eq1 = QuadraticEquation()
# прямий доступ до даних (потенційно небезпечно)
eq1.a = 1.0
eq1.b = -2.0
eq1.c = 1.0

second_eq = QuadraticEquation()
# доступ до даних об'єкта під "наглядом" створеного нами "посередника"
second_eq.set_data(1.0, -2.0, 0.0)

eq1.solve_q_equation()
second_eq.solve_q_equation()