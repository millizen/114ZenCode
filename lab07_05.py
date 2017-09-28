while True:
    num = int(input("Enter a number: "))
    if num == 0:
        print("End of program, goodbye.")
        break
    if num <= 1:
        print("Invalid input, try again.")
        continue
    x = 1
    count = 0
    while True:
        if num % x == 0:
            count += 1
        if x > num:
            break
        x += 1
    if count == 2:
        print("%d is a prime number."%num)
    elif count != 2:
        print("%d is not a prime number."%num)
