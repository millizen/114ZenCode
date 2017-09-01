x = input('Enter your buffet choice: ')
y = input('Is today Wednesday (yes/no)? ')
if(x != "Korean" and x != "Japanese"):
	print('Sorry, there is no Thai buffet.')
else :
	if(y == yes):
		a = (85/100)*x
		print("Your payment is %.2f Baht."%a)
	else:
		print("Your payment is %.2f Baht."%x)