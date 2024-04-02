a = [1, -10, 25, 31]

print(a)
b = a.__iter__()
print(b)
#for m in dir(a):
#    print(m)

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

#for el in a:
#    print(el)