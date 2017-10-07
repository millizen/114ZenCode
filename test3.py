number = int(input())
ans = 1

if number > 4000000000:
    pass

else:
    while number > 0:
        a = number % 10
        if a % 2 == 0:
            ans = ans * a
        number = number // 10

    if ans == 0:
        print(-1)
    else:
        print(ans)
