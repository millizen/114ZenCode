num = int(input())
day = int(input())

if num > 7 or num <= 0 or day <= 0 or day > 31:
	print("ERROR")
else:
	a = day - num
	if a % 7 == 0:
		s = "Sunday"
	if a % 7 == 1:
		s = "Monday"
	if a % 7 == 2:
		s = "Tuesday"
	if a % 7 == 3:
		s = "Wednesday"
	if a % 7 == 4:
		s = "Thursday"
	if a % 7 == 5:
		s = "Friday"
	if a % 7 == 6:
		s = "Saturday"
	print(s)
