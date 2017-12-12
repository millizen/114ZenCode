num = int(input())
ls = []
lsrm = []
for i in range(num):
    x = int(input())
    if x not in ls:
        if x > 0:
            ls.append(x)
ls.sort()
ans = []
for i in range(len(ls)-1):
    a = ls[i + 1] - ls[i]
    ans.append(a)
# print(ls)
# print(ans)
c = ans.count(min(ans))
for i in range(c):
    minn = min(ans)
    # print("minn =",minn)
    index = ans.index(minn)
    # print("index =",index)
    print("%d %d"%(ls[index],ls[index]+minn))
    ans.pop(index)
    ls.pop(index)
