N = 110
x = 0.12

def seqgen():
    a = 1.
    for n in range(1, N+1):
        a = a * x / n
        yield a

v = seqgen()
for el in v:
    print(el)
