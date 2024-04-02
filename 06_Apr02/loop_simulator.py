a = [1, -10, 25, 31]

# for i in range(len(a)):
#     print(a[i])
# print('-------')
#
#
# i = 0
# while i<len(a):
#     print(a[i])
#     i += 1
#     del i
# print('-------')



print(a)
b = a.__iter__()
print(b)
#for m in dir(a):
#    print(m)
# iteratable -- a
# iterator -- b

print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

#for el in a:
#    print(el)