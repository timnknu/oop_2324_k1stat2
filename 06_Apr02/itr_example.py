class SqNumCreator: # iterator
    def __init__(self, nfinal):
        self._k = 0
        self._max_k = nfinal
    def __next__(self):
        #print('__next__ is called', self)
        self._k += 1
        if self._k < self._max_k:
            return self._k**2
        else:
            raise StopIteration

class MyClass: # iteratable
    def __init__(self, n):
        self._max_num = n
    def __iter__(self):
        #print('>> __iter__ called from', self)
        return SqNumCreator(self._max_num)

if __name__ == "__main__":
    sq = MyClass(3)

    for num in sq: # b1 = iter(sq)
        # num = next(b1)
        for el in sq: # b2 = iter(sq)
            # el = next(b2)
            print(num, el)




