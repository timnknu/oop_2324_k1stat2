
import traceback

class ProtectedDictIntError(KeyError):
    def __init__(self, a):
        super().__init__()
        self._wrong_key = a
    def __str__(self):
        return f"помилка -- ключ {self._wrong_key} не є цілим числом"

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
            raise ProtectedDictIntError(key)
#
if __name__ == "__main__":
    d = ProtectedDictInt()
    try:
        d[1] = 2.0
        d[1.1] = 3.0
        print(d)
    except ProtectedDictIntError as e:
        print('наше виключення')
        print(e)
        print(e._wrong_key)
        print('на рядку', e.__traceback__.tb_lineno)
        print('---')
        s = traceback.format_exc()
        print('а ось яким було б стандартне повідомлення', s)
        print('---')
    except ZeroDivisionError:
        print('ділення на нуль')
    print('done')