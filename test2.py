number = int(input('Enter a number: '))
num = number
b = ''
a = ''
count = 0
x = 0
if number <= 0 or number > 26:
    print('Invalid input, program terminates.')
else:
    while x < (number - 1):
        a = a + chr(ord('A') + count)
        print(a)
        count = count + 1
        x = x+1
        if x == (number - 1):
            while num >= 1:
                count2 = 0
                while count2 < num:
                    b = chr(ord('A') + count2 )
                    print(b, end='')
                    count2 = count2 + 1
                print()
                num = num - 1
        else:
            pass
