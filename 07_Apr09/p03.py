# D_n = b * D_(n-1) - c * a * D_(n-2)
# D_1 = b
# D_2 = b**2 - a*c (або формально D_0 = 1)

def Dn_gen(a, b, c):
    # D_current = b * D_prev - c * a * D_prevprev
    D_prevprev = 1
    yield D_prevprev # D1
    D_prev = b
    yield D_prev # D2
    while True:
        D_current =  b * D_prev - c * a * D_prevprev
        yield D_current
        D_prevprev, D_prev = D_prev , D_current


v = Dn_gen(2, 5, 3)
for k, el in zip(range(10), v):
    print(k, el)