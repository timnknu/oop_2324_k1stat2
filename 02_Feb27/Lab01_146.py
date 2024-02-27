with (open('input01.txt') as f):
    for line in f:
        data = line.strip().split()
        if len(data):
            assert len(data)==2
            pwr = int(data[0])
            coef = float(data[1])
            print(pwr, coef)