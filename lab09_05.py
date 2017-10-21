def fibo(n):
    count = 0
    a0 = -1
    a1 = 0
    while True:
        summ = a0 + a1
        a0 = a1
        a1 = summ
        count += 1
        if count == n:
            break
    return int(summ * -1)



n = int(input("Enter n: "))
# print(fibo(n))
print("fibo(%d) = %d" %(n, fibo(n)))
