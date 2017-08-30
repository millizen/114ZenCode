h = int(input('Enter number of hours: '))
m = int(input('Enter number of minutes: '))
if(h < 0 or m < 0 or m > 59):
    print("Input Error")
else:
    baht = 0
    if(h == 0 and m <= 15):
        print('No charge, thanks.')
    else:
        if(m > 0):
            #if(m == 0)
            h = h + 1
            if(h <= 2):
                baht = baht + 10
                print('Total amount due is %d Bahts.'%baht)
            elif(h > 2):
                baht = baht + 10 + (10*(h-2))
                print('Total amount due is %d Bahts.'%baht)
        elif(m == 0):
            if(h <= 2):
                baht = baht + 10
                print('Total amount due is %d Bahts.'%baht)
            elif(h > 2):
                baht = baht + 10 + (10*(h-2))
                print('Total amount due is %d Bahts.'%baht)
