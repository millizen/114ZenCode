def summ(n):
    if n>0:
        f =0
        s =0
        for i in range(1,n+1):
            if i%2 == 0:
                s -= i
            else:
                f += i
        c = f+s
        return c

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to %d is %d" %(n,summ(n)) )
