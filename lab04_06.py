x = int(input('Enter year: '))
if x%4 == 0:
    if x%100 != 0:
        print('%d is not a leap year.'%x)
    else:
        print('%d is a leap year.'%x)
elif x%400 == 0:
    print('%d is a leap year.'%x)
