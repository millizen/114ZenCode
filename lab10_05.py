x = input()
y = input()
count = 0
ls = []
r = x.lstrip('[')
l = r.rstrip(']')
if len(l) == 0:
    ee = 0
else :
    for a in y:
        ls.append(a)
    # print(ls)
    for i in l:
        if i in ls:
            count += 1

    ee = (100/len(l)) * count
print(count)
print('%.2f'%ee)
