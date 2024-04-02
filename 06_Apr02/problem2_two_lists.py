class ElementExtractor: # iterator
    def __init__(self, col):
        self._move_number = 0 # номер ходу
        self._playerA = True # False => player B
        self._collection_owner = col # col -- об'єкт класу MyClass,
                                     # в якому "живуть" обидва списки
    def __next__(self):
        if self._playerA:
            lst = self._collection_owner._lstA
            #альтернатива -- if self._move_number >= min(len(self._collection_owner._lstA), len(self._collection_owner._lstB)):
            if self._move_number >= len(lst):
                raise StopIteration
            result = lst[self._move_number]
            self._playerA = False # підготуватися до наступної ітерації
            return result
        else:
            lst = self._collection_owner._lstB
            #альтернатива -- if self._move_number >= min(len(self._collection_owner._lstA), len(self._collection_owner._lstB)):
            if self._move_number >= len(lst):
                raise StopIteration
            result = lst[self._move_number]
            self._playerA = True # підготуватися до наступної ітерації
            self._move_number += 1
            return result
    #

class MyClass: # iteratable (він же колекція)
    def __init__(self, listA, listB):
        self._lstA = listA
        self._lstB = listB
    def __iter__(self):
        return ElementExtractor(self)


if __name__ == "__main__":
    thelog = MyClass(
        ['e4 d6', 'Nc3 e5',    'Bc4 Be7'],
        ['d4 Nf6', 'Nf3 Nbd7', '0–0 c6']
    )

    for mov in thelog:
        print(mov)

# Очікуваний результат:
# e4 d6
# d4 Nf6
# Nc3 e5
# Nf3 Nbd7
# Bc4 Be7
# 0–0 c6