x = int(input())
li = []
while True:
    a = x % 2
    x = x // 2
    li.append(a)
    if(x == 0):
        break
li.reverse()
for i in range(len(li)):
    print(li[i],end='')
