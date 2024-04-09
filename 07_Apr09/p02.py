def seqgen(x):
    a = 1.
    n = 1
    yield a
    while True:
        a = a * x / n
        n += 1
        yield a
#

N = 11
v = seqgen(0.12)
b = iter(v)
for k in range(N):
    el = next(b)
    print(el)
