import abc

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

if __name__ == "__main__":
    #s = SequenceAnalyzer() # не працює
    s = SinSeq() # працює!
    print(s)

