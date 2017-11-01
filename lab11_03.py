maxx = -9999
ls = []
while True:
    x = input()
    if x == '-1':
        break

    # for check max string
    l = x.split('=',1)
    r = len(l[0].strip())
    if r > maxx:
        maxx = r

    # add to ls list for print
    ls.append(l[0].strip())
    ls.append(l[1].strip())

# print(maxx)
# print(ls)

# loop for print
cc = 0
while cc < len(ls):
    if cc%2 == 0:
        print(ls[cc].rjust(maxx),end='')
        print(' = ',end='')
    if cc%2 != 0:
        print('%s'%ls[cc])
    cc += 1



# test case
# erwerer =eeee
#    ww =  r
# wer     eqwer=rr
