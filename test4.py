ls = [2,3,3,4,2,4,1]
ls1 = []

for i in ls:
    if i not in ls1:
        ls1.append(i)
print(ls1)
