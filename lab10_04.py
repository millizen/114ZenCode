x = input()
l = len(x)
count = 0
while True:
    y = input()
    if y == "0":
        break
    for i in x:
        if i == y:
            count += 1

print("%d/%d"%(count, l))
