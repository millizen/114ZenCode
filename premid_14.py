count = 0
s = ''
target = 3434534
while True:
    one = int(input(""))
    two = int(input(""))
    if one <= 0 or one > 6 or two <= 0 or two > 6:
        print("ERROR")
    else:
        count += 1
        # print(s)
    summ = one + two
    if summ == target:
        s = 'W'
    if summ == 4 or summ == 5 or summ == 6 or summ == 8 or summ == 9 or summ == 10:
        if count == 1:
            target = summ
            # print("target =",target )
    if summ == 7 or summ == 11:
        if count == 1:
            s = 'W'
        elif summ == 7:
            s = 'L'
    if summ == 2 or summ == 3 or summ == 12:
        if count == 1:
            s = 'L'
    if s == 'W' or s == 'L':
        break
print(count,end = ' ')
print(summ,end = ' ')
print(s)
