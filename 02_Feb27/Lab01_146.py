class Polynom:
    def __init__(self):
        self._coefs_dict = {}
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

obj = Polynom()
obj.read_from_file('input01.txt')
#obj.read_from_keyboard()
val = obj.evaluate_at_point(0.5)
print(val)
obj.show()
