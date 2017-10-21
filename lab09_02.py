def factor_count(n):
    d = 1
    c = 0
    while d<=n:
        if n%d == 0:
            c +=1
        d +=1
    return c

n = int(input("Enter n: "))
c = factor_count(n)
print(c)
