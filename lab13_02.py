num = int(input())
ans = []
if num >= 1 or num <= 100:
    for i in range(num):
        x = input()
        x = x.upper()
        x = x.replace('A','1')
        x = x.replace('J','10')
        x = x.replace('Q','10')
        x = x.replace('K','10')
        l = x.split()
        if len(l) == 5:
            summ = 0
            for i in l:
                i = int(i)
                summ += i
                if summ >= 16:
                    if summ > 21:
                        a = "busted"
                        ans.append(a)
                    else:
                        a = summ
                        ans.append(a)
                    break
for i in ans:
    print(i)
