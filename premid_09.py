num = int(input())
count = 0
minn = 99999
x = 0
while True:
    x = x + 1
    if num % x != 0:
        continue
    y = num / x
    p = x + y
    if p < minn :
        minn = p
    if x == num:
        break
print("%d"%minn)
