class Polynom:
    def __init__(self):
        self._coefs_dict = {}
    #def get_power(self):
    #    return self._coefs_dict.keys()
    def get_coef(self, pwr):
        #return self._coefs_dict.get(pwr, 0)
        if pwr in self._coefs_dict:
            return self._coefs_dict[pwr]
        else:
            return 0.0
    #

    def _process_line(self, line):
        data = line.split()
        if len(data):
            assert len(data) == 2
            try:
                pwr = int(data[0])
            except:
                print('Incorrect power:', line[0])
                return False
            #
            assert pwr >= 0
            try:
                coef = float(data[1])
            except:
                print('Incorrect coef:', line[1])
                return False
            #
            self._coefs_dict[pwr] = coef
            return True
    #
    def read_from_file(self, file_name):
        self._coefs_dict = {}
        try:
            with open(file_name) as f:
                for line in f:
                    self._process_line( line.strip() )
        except:
            print("Error while reading from file")
    #

    def read_from_keyboard(self):
        self._coefs_dict = {}
        print("Input powers & coefs, one pair per line, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line( s )
    #

    def evaluate_at_point(self, x):
        result = 0
        for pwr, coef in self._coefs_dict.items():
            term = x ** pwr * coef
            result += term
        return result
    #

    def show(self):
        print(self._coefs_dict)

    @staticmethod
    def add(poly1, poly2):
        powers1 = poly1._coefs_dict.keys()
        powers2 = poly2._coefs_dict.keys()
        for pwr in set(powers1) | set(powers2):
            coef = poly1.get_coef(pwr) + poly2.get_coef(pwr)

obj = Polynom()
obj.read_from_file('input01.txt')
#obj.read_from_keyboard()
#val = obj.evaluate_at_point(0.5)
#print(val)
#obj.show()
Polynom.add(obj, obj)
