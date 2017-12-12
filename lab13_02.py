# num = int(input())
# lscp = []
# ans = []
# y = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
# if num >= 1 and num <= 100:
#     for i in range(num):
#         d = ''
#         ls = []
#         lscp = []
#         lsm = []
#         x = input()
#         ls = x.split()
#         # print(ls)
#         for i in ls:
#             lscp.append(i)
#         for i in ls:
#             if i not in y:
#                 lscp.remove(i)
#         for i in lscp:
#             d += i + ' '
#         d = d.replace('A','1')
#         d = d.replace('J','10')
#         d = d.replace('K','10')
#         d = d.replace('Q','10')
#         # print(d)
#         lsm = d.split()
#         # print(lsm)
#
#         summ = 0
#         for i in lsm:
#             i = int(i)
#             summ += i
#             if summ >= 16:
#                 break
#         ans.append(summ)
#
# for i in ans:
#     if  i > 21:
#         print('busted')
#     else:
#         print(i)
#================================================================
line = int(input())
count = 1
ls = []
while count <= line:
    a = []
    bj = str(input())
    a.append(bj)
    ls.append(a)
    count += 1
chck = []
for x in ls:
    b = ''
    chck2 = []
    for y in x:
        for z in y:
            if z == ' ':
                chck2.append(b)
                b = ''
            else:
                b += z
    chck2.append(b)
    chck.append(chck2)
ans = []
for z in chck:
    e = 0
    for q in z:
        if e > 16:
            break
        else:
            if q == 'A':
                e += 1
            elif q == 'J' or q == 'Q' or q == 'K':
                e += 10
            elif q.isdigit() == True:
                e += int(q)
    ans.append(e)
for p in ans:
    if p > 21:
        print('busted')
    else:
        print(p)
