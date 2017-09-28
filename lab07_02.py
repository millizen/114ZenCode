x = int(input("Enter a number: "))
s = x
if x <= 0 or x > 26:
    print("Invalid input, program terminates.")
else:
    while True:
        count = 1
        while count <= s:
            a = chr(ord('A') + (count-1))
            print(a, end='')
            count += 1
        print()
        s -= 1
        if s == 0:
            break
