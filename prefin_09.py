num = int(input())
ls = []
ls1 = []
dnum = num / 2
for i in range(num):
    x = input()
    ls.append(x)
# print(ls)
for i in ls:
    a = ls.count(i)
    ls1.append(a)
# print(ls1)
maxx = max(ls1)
if maxx > dnum:
    index = 0
    for i in ls1:
        if i == maxx:
            break
        index += 1
    # print(index)
    print(ls[index])
else:
    print(0)
