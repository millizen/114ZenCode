x = input()
y = input()
count = 0
ls = []
r = x.lstrip('[')
l = r.rstrip(']')
for a in y:
    ls.append(a)
# print(ls)
for i in l:
    if i in ls:
        count += 1

ee = (100/len(l)) * count
print(count)
print('%.2f'%ee)
