import abc

class SequenceAnalyzer: #(metaclass=abc.ABCMeta):
    #@abc.abstractmethod
    def terms_gen(self):
        pass
        a = 1
        n = 1
        yield (n, a)
        while True:
            # або замість двох yield можна було поставити один yield (n, a), але тут
            a = -a / (n+1) / (n+2)
            n += 2
            yield (n, a)

    # def __str__(self):
    #     n = 10
    #     s = "string representation"
    #     return s

s = SequenceAnalyzer()
v = s.terms_gen()
for el in v:
    print(el)

