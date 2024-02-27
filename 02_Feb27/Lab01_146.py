poly = {}
with open('input01.txt') as f:
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
print(poly)
