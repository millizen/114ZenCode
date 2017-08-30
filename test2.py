x = int(input("What number do you want to change.(best 10): "))
y = int(input("What best do you want to change to.(best 2-9): "))
li = []
while True:
    a = x % y
    x = x // y
    li.append(a)
    if(x == 0):
        break
li.reverse()
for i in range(len(li)):
    print(li[i],end='')
