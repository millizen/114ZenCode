x = int(input('Enter year: '))
if (x > 0):
	if x%4 == 0 and x%100 != 0:
	    print('%d is a leap year.'%x)
	elif x%400 == 0:
	    print('%d is a leap year.'%x)
	else:
	    print('%d is not a leap year.'%x)
else :
	print('Invalid year.')