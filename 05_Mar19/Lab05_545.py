import copy

class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            # дані self <- дані з n
            #copy.deepcopy()
            self._data = n._data
        else:
            self._data = [0.0]*n

# a = Vector(3)
# b = Vector(a)

x = [1,2,3]
y = x
y[0] = -100
print(x)


x = [1,2,3]
y = copy.deepcopy(x)
y[0] = -100
print(x)