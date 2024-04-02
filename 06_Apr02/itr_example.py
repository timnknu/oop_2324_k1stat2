class SqNumCreator:
    def __init__(self):
        self._storage = ['a', 'y', 'b', -10]
        self._k = 0
    def __next__(self):
        elem = self._storage[self._k]
        self._k += 1
        return elem

class MyClass:
    def __iter__(self):
        return SqNumCreator()

if __name__ == "__main__":
    sq = MyClass()

    for num in sq: # b1 = iter(sq)
        # num = next(b1)
        for el in sq: # b2 = iter(sq)
            # el = next(b2)
            print(num, el)




