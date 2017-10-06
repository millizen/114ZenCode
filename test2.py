x = int(input())
div = 10
while True:
    a = x % div
    b = a // (div/10)
    div = div * 10
    print('%d'%b)
    if a == x:
        break
