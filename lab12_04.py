count = 0
ls = []
ls1 = []
lls = []
while count < 20:
    x = int(input("Enter score: "))
    if x < 0 or x > 10:
        print("Score is out of range.")
    else:
        count += 1
        ls.append(x)

print("-----\nOriginal list:")
print(ls)
for i in ls:
    ls1.append(ls.count(i))
maxx = max(ls1)
# print(maxx)
# print(ls1)
print("Mode of scores:")
n = 0
for j in ls1:
    if j == maxx:
        if ls[n] not in lls:
            print(ls[n])
        lls.append(ls[n])

    n += 1
# print(lls)
