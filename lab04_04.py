x = input('Enter your buffet choice: ')
KindOfStore = ['Korean','Japanese']
Price = [1500.00,1000.0]
count = -1
for i in KindOfStore:
	count += 1
	if x == KindOfStore[count]:
		y = input('Is today Wednesday (yes/no)? ')
		if y == 'yes':
			z = Price[count]
			z1 = z*(85/100)
			print('Your payment is %.2f Baht.'%z1)
		if y == 'no':
			print('Your payment is %.2f Baht.'%(Price[count]))
		break
	elif count == len(KindOfStore)-1:
		print("Sorry, there is no %s buffet."%x)
