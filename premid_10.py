x = int(input())
y = 10
summ = 0
while True:
    a = (x % y)
    b = a // (y/10)
    # print(b)
    if b % 2 != 0:
        summ = summ + b
    y = y * 10
    if a == x:
        break
if summ > 0:
    print('%d'%summ)
elif summ == 0:
    print(-1)
