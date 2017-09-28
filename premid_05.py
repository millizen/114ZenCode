num = int(input("Enter a number: "))
di = int(input("Enter a digit: "))
if num < 0 or di > 9 or di < 0:
    if num < 0:
        print("Invalid number.")
    if di > 9 or di < 0:
        print("Invalid digit.")
else :
    x = 1
    count = 0
    while True:
        x *= 10
        y = num % x
        z = y // (x/10)
        if z == di:
            count += 1
        if y == num:
            break
    if count == 1 :
        print("Digit %d occurs %d time."%(di,count))
    else :
        print("Digit %d occurs %d times."%(di,count))
