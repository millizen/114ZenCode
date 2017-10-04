x = int(input())
c = x**2
a = 1
b = 1
count = 0
while a < x:
    a += 1
    b = 1
    while b < x:
        b += 1
        if a**2 + b**2 == c:
            count += 1
print(count//2)
