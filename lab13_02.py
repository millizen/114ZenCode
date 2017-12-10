num = int(input())
lscp = []
ans = []
y = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
if num >= 1 and num <= 100:
    for i in range(num):
        d = ''
        ls = []
        lscp = []
        lsm = []
        x = input()
        ls = x.split()
        # print(ls)
        for i in ls:
            lscp.append(i)
        for i in ls:
            if i not in y:
                lscp.remove(i)
        for i in lscp:
            d += i + ' '
        d = d.replace('A','1')
        d = d.replace('J','10')
        d = d.replace('K','10')
        d = d.replace('Q','10')
        # print(d)
        lsm = d.split()
        # print(lsm)

        summ = 0
        for i in lsm:
            i = int(i)
            summ += i
            if summ >= 16:
                break
        ans.append(summ)

for i in ans:
    if  i > 21:
        print('busted')
    else:
        print(i)
