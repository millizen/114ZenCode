num = int(input())
ls = []
count = 0
while True:
    x = int(input())
    ls.append(x)
    count += 1
    if count == num:
        break
mon = int(input())
ls.sort(reverse=True)
for i in ls:
    o = mon // i
    o1 = o * i
    mon = mon - o1 
    print("%d: %d"%(i,o))
