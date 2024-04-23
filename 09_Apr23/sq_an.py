import abc
import math

class SequenceAnalyzer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def terms_gen(self):
        pass

    def __str__(self):
        N = 10
        s = "elements:\n"
        for k, ak in self.terms_gen():
            s += f"a_({k}) = {ak}\n"
            if k > N:
                break
        return s

    def eval(self, x):
        eps = 1e-5 # те саме, що і 10**(-5)
        sm = 0
        for k, ak in self.terms_gen():
            term = ak * x**k
            if abs(term) < eps:
                break
            sm += term
        return sm


class SinSeq(SequenceAnalyzer):
    def terms_gen(self):
        a = 1
        n = 1
        yield (n, a)
        while True:
            # або замість двох yield можна було поставити один yield (n, a), але тут
            a = -a / (n + 1) / (n + 2)
            n += 2
            yield (n, a)

class CosSeq(SequenceAnalyzer):
    def terms_gen(self):
        a = 1
        n = 0
        yield (n, a)
        while True:
            a = -a / (n + 1) / (n + 2)
            n += 2
            yield (n, a)


def print_table(objs, a=0, b=1, npoints=10):
    # a    == x[1]
    # a+s  == x[2]
    # a+2s == x[3]
    # ...
    # b    == x[npoints] = a + s*(npoints-1)
    s = (b-a)/(npoints-1)
    # x[i] == a + s*(i-1)
    for i in range(1, npoints+1):
        x = a + s*(i-1)
        print(f"x_{i} = {x}: (f1, f2, ...)")
#


print_table([], a=-1, b=1)
print('----')

if __name__ == "__main__":
    #s = SinSeq()
    s = CosSeq()
    print(s.eval(2.0))
    print(math.cos(2.0))

