import math

def seqgen(x, eps):
    a = 1.
    n = 1
    yield a
    while a > eps:
        a = a * x / n
        n += 1
        yield a
#

x = 1.2

v = seqgen(x, 1e-3)
y = 0.0
for el in v:
    y += el
    print(el, 'y =',y)

print('math:', math.exp(x))