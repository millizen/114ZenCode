x = int(input('How many TVs? '))
y = int(input('How many DVD players? '))
z = int(input('How many Audio Systems? '))

if (x >= 0 and y >= 0 and z >= 0):
	TotalPrice = (x * 6000) + (y * 1500) + (z * 3000)
	print("Total price is %.2f baht."%TotalPrice)
	if (TotalPrice >= 24000):
		a = (20/100)*TotalPrice
		TotalPrice = (80/100)*TotalPrice
		print("You've got a discount of %.2f baht."%a)
print("Your payment is %.2f baht. Thank you!"%TotalPrice)











