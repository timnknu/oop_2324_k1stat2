class MyClass:
    def __init__(self):
        self._storage = ['a', 'y', 'b', -10]
        self._k = 0
    def __iter__(self):
        return self
    def __next__(self):
        elem = self._storage[self._k]
        self._k += 1
        return elem

if __name__ == "__main__":
    sq = MyClass()

    for num in sq: # b1 = iter(sq)
        # num = next(b1)
        for el in sq: # b2 = iter(sq)
            # el = next(b2)
            print(num, el)




# class SqNumCreator:
#     def __next__(self):
#         return -10
