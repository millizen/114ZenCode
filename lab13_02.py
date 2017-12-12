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
size = input()
p = int(input())
s = []
q = ''
if size.count('x')==1:
    for x in size:
        if x != 'x':
            q += x
        else:
            if int(q) >= 0:
                s.append(int(q))
                q = ''
    s.append(int(q))
    if p <= s[0]*s[1]:
        ls = []
        ls2 = []
        for x in range(p):
            xy = input()
            ls.append(xy)
        for x in ls:
            ld = []
            a = ''
            for y in x:
                if y != ',':
                    a += y
                else:
                    ld.append(int(a))
                    a = ''
            ld.append(int(a))
            if ld[0]>=0 and ld[1] >= 0 and ld[0]<= s[0]-1 and ld[1] <= s[1]-1:
                ls2.append(ld)
        for x in range(s[0]):
            for y in range(s[1]):
                if [x,y] in ls2:
                    print('*',end='')
                else:
                    c = 0
                    if [x-1,y-1] in ls2 :
                        c+=1
                    if [x-1,y] in ls2 :
                        c+=1
                    if [x-1,y+1] in ls2 :
                        c+=1
                    if [x,y-1] in ls2 :
                        c+=1
                    if [x,y+1] in ls2 :
                        c+=1
                    if [x+1,y-1] in ls2:
                        c+=1
                    if [x+1,y] in ls2:
                        c+=1
                    if [x+1,y+1] in ls2:
                        c+=1
                    print(c,end='')
            print()
