def f():
    #.....
    for j in range(10):
        yield j**2
    #....

v = f()
print(v)
for elem in v:
    print(elem)