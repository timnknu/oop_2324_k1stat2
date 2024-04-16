class ProtectedDictInt:
    def __init__(self):
        self._data = {}
    def __str__(self):
        return str(self._data)
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        if isinstance(key, int):
            self._data[key] = value
        else:
            print('Error')

d = ProtectedDictInt()
d[1] = 2.0
d[1.1] = 3.0
print(d)