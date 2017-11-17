x = input()
if len(x) == 1 or len(x) == 0:
    print(x)
else:
    if len(x) % 2 != 0:
        l = len(x)
        ll = len(x) - 1
        lll = int(len(x) / 2)
        index = 0
        s = ''
        while True:
            s = s + x[index]
            s = s + x[ll - index]
            index += 1
            if index == lll:
                break
        s = s + x[lll]
        print(s)

    elif len(x) % 2 == 0:
        l1 = len(x)
        ll1 = len(x) - 1
        lll1 = int(len(x) / 2)
        index1 = 0
        s1 = ''
        while True:
            s1 = s1 + x[index1]
            s1 = s1 + x[ll1 - index1]
            index1 += 1
            if index1 == lll1:
                break
        print(s1)
