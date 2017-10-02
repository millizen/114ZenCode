num = int(input('Enter a number: '))
if num < 0:
    print('Invalid input, program terminates.')
else:
    count = 0

    while True:
        if count == 0:
            print("0! = 1 = 1")
            count += 1
        if count == num+1:
            break
        if count > 0:
            print("%d! = "%count,end='')
            c = count
            s = ''
            summ = 1
            while True:

                s = s + str(c)
                if c == 1:
                    s = s + ' = '
                else :
                    s = s + ' x '
                summ *= c
                c -= 1
                if c == 0:
                    break
            print(s,end='')
            print(summ)
            count += 1
