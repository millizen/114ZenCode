see = 0
maxx = -1
while True:
    x = int(input())
    if x > maxx:
        see = see + 1
        maxx = x
    if x == -1:
        break
print(see)
