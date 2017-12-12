def aa(ls,ss):
    summ = []
    n = len(ls)
    while n != 0:
        ls1 = []
        for i in range(0,n):
            ls1.append(ls[i])
        summ.append(sum(ls1))
        n -= 1
    for i in ss:
        summ.append(i)
    return(summ)
ls = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ls.append(x)
summ = []
while ls != []:
    summ = aa(ls,summ)
    ls.remove(ls[0])
print(summ)
print(max(summ))
