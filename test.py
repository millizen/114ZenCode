number = int(input("Enter a number: "))
x = 1
i = 0
a = ''
if number <= 0 or number > 26:
    print("Invalid input, program terminates.")
else:
    while x <= number:
        a = a + chr(ord('A') + i)
        print(a)
        i += 1
        x += 1
