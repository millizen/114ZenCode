x1 = input()
x2 = input()
x1.strip()
x2.strip()
l1 = len(x1) #ตัวยาว
l2 = len(x2) #ตัวสั้น
if l1 == 0 or l2 == 0:
    print('0-0')
else:
    if l1 < l2:
        a = x2
        x2 = x1
        x1 = a
        b = l2
        l2 = l1
        l1 = b
    index = 0
    same = 0
    while index < l2:
        if x2[index] == x1[index]:
            same += 1
        index += 1
    print(same,end='')
    print('-',end='')
    have = 0
    ls = []
    for i in x2:
        if i not in ls:
            ls.append(i)
            if i in x1:
                have += 1
    have = have - same
    print(have)
