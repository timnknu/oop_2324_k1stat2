def f():
    #.....
    yield -15
    #....

v = f()
for nm in dir(v):
    print(nm)
print(v)