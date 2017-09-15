x = int(input())
div = 10
div1 = 10
summ1 = 0
while True:
    s = (x % div)
    a = s // (div/10)
    div = div * 10
    summ = summ + a
    if s == x :
        break
summ = int(summ)
print(summ)
while summ > 10:
    while True:
        ss = (summ % div1)
        aa = ss // (div1)
        div1 = div1 * 10
        summ1 = summ1 + aa
        if ss == summ :
            break
    summ = ss
