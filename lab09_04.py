def fac(n):
    if n>0:
        c = 1
        for i in range(1,n+1):
            c *= i
    if n == 0:
        c = 1
    return c


n = int(input("Enter n: "))
print(str(n)+'!', "=",fac(n))
