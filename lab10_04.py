x = input()
l = len(x)
count = 0
li = ''
while True:
    n = input()
    if n == '0':
        break
    if n not in li:
        for i in x:
            if i == n:
                count += 1
    li = li + n
print("%d/%d"%(count,l))
