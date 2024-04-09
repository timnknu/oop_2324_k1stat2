
def seqgen(x):
    a = 1.
    n = 1
    while True:
        a = a * x / n
        n += 1
        yield a
#

N = 11
v = seqgen(0.12)
k = 0
for el in v:
    k += 1
    if k > N:
        break
    print(el)
