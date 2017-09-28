num = int(input('Enter a number: '))
if num < 0:
    print('Invalid input, program terminates.')
else:
    st = -1
    while True:
        st += 1
        print(st)

        if num == st:
            break
