num = int(input())
div = 10
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
    # print("a =",a)
    print('%d'%ans)
