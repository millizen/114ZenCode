s = input()
l = len(s)
o = len(s)
if len(s) == 1:
    print(s)
elif l != 0:
    if l % 2 == 0:
        ll = l / 2
        ll = int(ll)
        ll2 = ll
        while True:
            print(s[ll-1],end='')
            ll = ll - 1
            if ll == 0:
                break
        # print(ll2)
        while True:
            print(s[o-1],end='')
            o = o - 1
            if o == ll2:
                break
    if l % 2 != 0:
        aa = l // 2
        aa1 = aa
        while True:
            print(s[aa-1],end='')
            aa = aa - 1
            if aa == 0:
                break
        print(s[aa1],end='')
        while True:
            print(s[l-1],end='')
            l = l - 1
            if l == aa1 + 1:
                break
