x = int(input())
y = 10
while True:
    a = (x % y) // (y/10)
    print(a)
    y = y * 10
    if a == 0:
        break
