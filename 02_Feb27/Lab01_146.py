class Polynom:
    def __init__(self):
        self._data = {}
    def read_from_file(self, file_name):
        poly = {}
        with open(file_name) as f:
            for line in f:
                data = line.strip().split()
                if len(data):
                    assert len(data)==2
                    try:
                        pwr = int(data[0])
                    except:
                        print('Incorrect power:', line[0])
                        continue
                    #
                    assert pwr >= 0
                    try:
                        coef = float(data[1])
                    except:
                        print('Incorrect coef:', line[1])
                        continue
                    #
                    poly[pwr] = coef
        self._data = poly
    def show(self):
        print(self._data)

obj = Polynom()
obj.read_from_file('input01.txt')
obj.show()
