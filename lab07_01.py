x = int(input("Enter a number: "))
if x <= 0 or x > 26:
    print("Invalid input, program terminates.")
else:
    a = ''
    i = 0
    count = 1
    while count <= x:
        a += chr(ord('A')+i)
        print(a)
        i += 1
        count += 1
