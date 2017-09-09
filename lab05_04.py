x = int(input())
div = 10
if x>0:
    while True:
        s = (x % div)
        a = s// (div/10)
        div = div * 10
        print('%d'%a)
        if s == x :
            break
else:
    print("ERROR")
