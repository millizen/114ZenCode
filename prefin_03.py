import math
s = input()
num = int(input())
lss = s.split(',')
l = len(lss)
lss1 = []
for i in lss:
    lss1.append(i)
lss1.pop(0)
if num <= len(lss):
    print(lss[num - 1])
elif num > len(lss):
    lss2 = []
    aa = num - len(lss)
    aa1 = math.ceil(aa / 7)
    c = 0
    while True:
        lss2 += lss1
        c += 1
        if c == aa1:
            break
    print(lss2[aa-1])
