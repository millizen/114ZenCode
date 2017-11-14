ls = []
maxx = -1
while True:
    x = int(input())
    if x == -1:
        break
    if x > maxx:
        ls.append(x)
        maxx = x
print(ls)
