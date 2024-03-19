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
        print('what is [',j,'] ?')
        return -100

a = Vector(3)
print(a['H'])