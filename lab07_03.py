x = int(input("Enter a number: "))
s = x
if x <= 0 or x > 26:
    print("Invalid input, program terminates.")
else:
    a = ''
    count = 1
    while count <= x:
        a += chr(ord('A') + (count-1))
        print(a)
        count += 1
    while True:
        count1 = 1
        while count1 <= s-1:
            a = chr(ord('A') + (count1-1))
            print(a, end='')
            count1 += 1
        print()
        s -= 1
        if s == 0:
            break

# a
# ab
# abc
# abcd
# abcde
# abcd
