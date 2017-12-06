# 3
# 5
# 8
# 13
# -1
# >> 22
##########################################
x = int(input("Enter input: "))
i = 0
a0 = -1
a1 = 0
while True:
    summ = a0 + a1
    a0 = a1
    a1 = summ
    print(summ * -1)
    i += 1
    if i == x:
        break
