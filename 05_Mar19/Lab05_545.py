import copy

class Vector:
    def __init__(self, n):
        if isinstance(n, Vector):
            # дані self <- дані з n
            self._data = copy.deepcopy(n._data)
        else:
            self._data = [0.0]*n
    def __len__(self):
        return len(self._data)
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        self._data[j] = val
    def __str__(self):
        s = 'Vec: '
        #s += ','
        for elem in self._data:
            s += str(elem) + ', '
        return s


# a = Vector(3)
# print(a[0])
# a[0] = 1.2
# print(a)

print('!?'.join(['yya', str(1), 'efg']))