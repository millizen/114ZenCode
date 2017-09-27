x = int(input())
div = 10
if x<= 10:
	print("ERROR")
else:
	while True:
		dx = x%div
		ans = dx//(div/10)
		print("%d" %ans)
		div = div*10
		if dx == x:
			break
