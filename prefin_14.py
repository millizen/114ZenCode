ls = []
while True:
    x = int(input())
    if x == 0:
        break
    else:
        ls.append(x)
print(ls)
ls1 = []
num = 0
while num < len(ls):

    for i in range(num,len(ls)):
        print(i)
    num += 1
    print('======')
