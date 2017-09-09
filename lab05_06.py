count = 0
while True:
    x = int(input('Enter number: '))
    if x < 0 :
        break
    else :
        if (x % 2) != 0:
            count += 1
print('Received %d odd numbers'%count)
