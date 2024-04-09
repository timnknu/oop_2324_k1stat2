def f():
    #.....
    for j in range(10):
        yield j**2
    #....

v = f()
b = iter(v)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))