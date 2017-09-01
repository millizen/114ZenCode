target = 72
number = int(input("Enter your guess (0 - 100): "))
if (number < 0 or number > 100) :
	print('Sorry, out of range, try again later.')
else:
	if (number < target):
		print('Sorry, your guess is too low, try again later.')
	elif (number == target) :
		print('Congratulations, your guess is correct.')
	elif (number > target) :
		print('Sorry, your guess is too high, try again later.')
