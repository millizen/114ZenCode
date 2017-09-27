x = int(input())
y = 10
summ = 1

while True:
    a = (x % y)
    b = a // (y/10)
    # print(a)
    y = y * 10
    if a == x:
        break
    # print(b)
    if b % 2 == 0:
        summ = summ * b
# print(summ)
if summ == 1:
    print(-1)
elif summ >= 0:
    print('%d'%summ)
