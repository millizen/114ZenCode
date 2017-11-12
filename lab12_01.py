count = 0
ls = []
ls1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
while count < 20:
    x = int(input("Enter score: "))
    if x < 0 or x > 10:
        print("Score is out of range.")
    else:
        count += 1
        ls.append(x)
print("Original list:")
print(ls)
for i in range(20):
    for j in ls:
        if i == j:
            ls1[i] += 1
for i in range(11):
    i = str(i)
    print(i.rjust(2),end=' ')
    i = int(i)
    print('%s'%('*'*ls1[i]))
