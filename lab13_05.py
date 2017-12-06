x = int(input())
c = input()
ls = []
i = 0
a0 = -1
a1 = 0
if x < 0 or c not in 'oOeE':
    print("ERROR")
else:
    while True:
        summ = a0 + a1
        a0 = a1
        a1 = summ
        ls.append(summ * -1)
        i += 1
        if i == x+1:
            break

    if c == 'e' or c == 'E':
        su = 0
        for i in range(len(ls)):
            if i%2 == 0:
                su = su + ls[i]
        print(su)
    elif c == 'o' or c == 'O':
        su1 = 0
        for i in range(len(ls)):
            if i%2 != 0:
                su1 = su1 + ls[i]
        print(su1)

    # print(ls)
