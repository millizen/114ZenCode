f = 1
count = 0
while True:
    print("Frame #",f)
    if f == 1 :
        x = int(input("Number of pins down: "))
    if x == 10 and f != 1:
        print(x)
        x =  int(input("Number of pins down: "))
        f += 1
    elif x < 10 :

        if count == 0:
            a = 10 - x
            print("Frame #",f)
            x =  int(input("Number of pins down (0-%d): "%a))
            count += 1
        elif count == 1:
            x =  int(input("Number of pins down: "))
            f += 1
            count -= 1
    if f == 10:
        break
