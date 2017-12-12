# num = int(input())
# ls = []
# lsrm = []
# for i in range(num):
#     x = int(input())
#     if x not in ls:
#         if x > 0:
#             ls.append(x)
# ls.sort()
# ans = []
# for i in range(len(ls)-1):
#     a = ls[i + 1] - ls[i]
#     ans.append(a)
# # print(ls)
# # print(ans)
# c = ans.count(min(ans))
# for i in range(c):
#     minn = min(ans)
#     # print("minn =",minn)
#     index = ans.index(minn)
#     # print("index =",index)
#     print("%d %d"%(ls[index],ls[index]+minn))
#     ans.pop(index)
#     ls.pop(index)



num = int(input())
c = 0
ls = []
for i in range(num):
    x = int(input())
    if x not in ls:
        ls.append(x)
print(ls)
ls.sort()
div = []
for i in range(len(ls)-1):
    d = ls[i+1] - ls[i]
    div.append(d)
print(div)
minn = min(div)
count = div.count(minn)
for i in range(count):
    index = div.index(minn)
    print("%d %d"%(ls[index],ls[index] + minn))
    ls.pop(index)
    div.pop(index)
