
class MyClass:
    def __iter__(self):
        #return 'XYZ'
        #pass
        return iter(['a', 'y', 'b', -10])


if __name__ == "__main__":

    sq = MyClass()

    for num in sq: # iter(sq) -> b
        # next(b) -> num
        print(num)
