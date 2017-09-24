f = 1
f1 = 1
score = 0
while True:
    if f1 == 1:
        print('Frame # %d'%f)
        x = int(input('  Number of pins down: '))
        score += x
        if x == 10:
            f += 1
            f1 += 1
        else :
            print('Frame # %d'%f)
            a = 10 - x
            x = int(input('  Number of pins down (0-%d): '%a))
            score += x
            f += 1
    if f1 == 2:
        # f += 1
        f1 -= 1
    if f == 11:
        break
print('Total score is %d'%score)
