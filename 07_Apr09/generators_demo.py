def f():
    #.....
    yield -15
    yield -25
    yield 100500

    #....

v = f()
for elem in v:
    print(elem)