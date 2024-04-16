class ProtectedDictInt:
    def __init__(self):
        pass
    def __getitem__(self, item):
        pass
    def __setitem__(self, key, value):
        pass

d = ProtectedDictInt()
d[1] = 2.0
d[1.1] = 3.0
print(d)