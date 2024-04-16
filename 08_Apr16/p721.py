class ProtectedDictIntError(KeyError):
    def __init__(self):
        super().__init__()

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
            raise ProtectedDictIntError()
#
if __name__ == "__main__":
    d = ProtectedDictInt()
    d[1] = 2.0
    d[1.1] = 3.0
    print(d)