#print(1.1 - 0.1 - 1.0)
#print(1.1 - 1.0 - 0.1)

p = 15.
for j in range(30):
    eps = 1/5.**j
    print(j, eps, ':', ((1+eps)**p - 1) / eps )