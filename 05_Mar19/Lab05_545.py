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
        print('SET:', j, val)

a = Vector(3)
print(a[0])
a['world'] = 'hello'
