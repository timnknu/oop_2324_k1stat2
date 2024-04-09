N = 110

def seqgen(x):
    a = 1.
    n = 1
    while True:
        a = a * x / n
        n += 1
        yield a

v = seqgen(0.12)
for el in v:
    print(el)
