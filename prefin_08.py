num = int(input())
ls = []
ls1 = []
ls2 = []
count = 0
while count != num:
    x = int(input())
    ls.append(x)
    count += 1

print(ls)
for i in ls:
    for j in ls:
        ls1.append(i)
        ls1.append(j)
print(ls1)
print('len ls1 = %s'%(len(ls1)))
n = 0
while True:
    div = abs(ls1[n] - ls1[n+1])
    ls2.append(div)
    n += 2
    if n == len(ls1)-2:
        break
print(ls2)
