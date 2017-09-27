x = int(input("Enter a number: "))
if x <= 0 or x > 26:
    print("Invalid input, program terminates.")
else:
    a = ''
    i = 0
    count = x
    while count >= 1:
        a += chr(ord('A') + i)
        i += 1
        count -= 1
    print(count)
    print(i)
    print(a)
