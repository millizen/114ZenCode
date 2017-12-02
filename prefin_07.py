import math
num = int(input())
s1 = input()
ls1 = s1.split()
lss1 = []
lss2 = []
for i in ls1:
    ni = int(i)
    d = math.ceil(ni/num)
    lss1.append(d)
    summ = sum(lss1)
    lss2.append(summ)
# print(lss1)
# print(lss2)
print(lss2[len(lss2)-1])
for i in lss2:
    print(i,end=' ')
