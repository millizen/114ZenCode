maxx = -9999
ls = []
while True:
    x = input()
    if x == '-1':
        break
    c = 0
    count = 0
    # loop for count max string
    while c < len(x):
        if x[c] != '=' and x[c] != ' ':
            count += 1
        else:
            break
        c += 1
    l = x.split('=',1)
    # print(l[0].strip())
    # print(l[1].strip())

    # add to ls list for print
    ls.append(l[0].strip())
    ls.append(l[1].strip())
    if count > maxx:
        maxx = count
# print(maxx)
# print(ls)

# loop for print
cc = 0
while cc < len(ls):
    if cc%2 == 0:
        print(ls[cc].rjust(maxx),end='')
        print(' = ',end='')
    if cc%2 != 0:
        print(' %s'%ls[cc])
    cc += 1
