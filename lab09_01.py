def check_prime(n):
    d = 2
    c = 0
    while d<=n:
        if c>1:
            break
        if n%d == 0:
            c +=1
        d +=1
    if c == 1:
        return True
    else:
        return False

n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")
