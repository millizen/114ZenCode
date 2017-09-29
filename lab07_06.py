x = int(input("Enter height: "))
y = int(input("Enter width: "))
if x <= 0 or y <= 0:
    print("Invalid input, program terminates.")
else:
    count = 0
    a = 0
    while True:
        if count == x:
            break
        count += 1
        if a == 1:
            a -= 1
            i2 = 0
            while True:
                print(' *',end='')
                i2 += 1
                if i2 == y:
                    break
        elif a == 0:
            i1 = 0
            while True:
                print('* ',end='')
                i1 += 1
                if i1 == y:
                    break
            a += 1
        print()
