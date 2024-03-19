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
        # тут можуть бути додаткові перевірки
        self._data[j] = val
    def __str__(self):
        s = 'Vec: '
        s += ', '.join(map(str, self._data))
        return s
    def __add__(self, other):
        res = Vector(len(self))
        if isinstance(other, Vector):
            # покомпонентна сума двох векторів
            pass
        else:
            # додавання числа до всіх компонент
            for i in range(len(res)):
                res[i] = self._data[i] + other
            return res


a = Vector(3)
print(a[0])
a[0] = 1.2
a = a + 1
print(a)

