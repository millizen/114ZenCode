z = int(input("Enter positive integer: "))
rr = z
if z == 0 or z < 0:
    print("Invalid number.")
elif z > 1:
    div = 1
    summ = 1
    while True :
        x = z % div
        x1 = z / div
        if x == 0:
            t = 1
            count = 0
            while True:
                if div % t == 0:
                    count += 1
                if t > div:
                    break
                t += 1
            if count == 2:
                z = z / div
                summ = summ * div
                print(div)
                # print(x1)
                div = 0
        div += 1
        if div == z:
            break
    w = rr/summ
    print("%d"%w)
