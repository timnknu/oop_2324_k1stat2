# class QuadraticEquation:
#     def __init__(self):
#
# прогоарам без класів і об'єктів, яка тим не менше слідує (деяким) принципам ООП
def solve_q_equation(data):
    D = data['b'] ** 2 - 4 * data['a'] * data['c']
    if D < 0:
        print('No solutions')
        return
    x1 = (-data['b'] + D**0.5)/(2 * data['a'])
    x2 = (-data['b'] - D ** 0.5) / (2 * data['a'])
    print(x1, x2)
#

eq1 = {'a': 1.0, 'b': -2.0, 'c': 1.0}
second_eq = {'a': 1.0, 'b': -2.0, 'c': 0.0}
solve_q_equation(eq1)
solve_q_equation(second_eq)

