num = int(input())
div = 10
summ = 1
while True:
    if num % div == num:
        d = div
    if num % div == num:
        break
    div *= 10

while True:
    a = num % d
    if d == 1:
        break
    ans = a // (d/10)
    d /= 10
    if ans % 2 == 0:
        summ = summ * ans

if summ == 1:
    print(-1)
elif summ >= 0:
    print('%d'%summ)
