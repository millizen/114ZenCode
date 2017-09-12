x = int(input("Enter height: "))
i = x+(x-2)
a = -1
while i >= 0:
    print(' '*(i),end='')
    print('1',end='')
    print(' '*a,end='')
    #print(i,end='')
    if i == x+(x-2):
        print('')
    else :
        print('1')
    i -= 2
    a += 4
