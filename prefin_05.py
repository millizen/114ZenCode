x = input()
x = x.lower()
x = x.strip()
count = 0
allp = "A"
if len(x) == 0 :
    print(0)
else:
    for i in x:
        if i > allp:
            count += 1
            allp = i
        else:
            break
    print(count)
