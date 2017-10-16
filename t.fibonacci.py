# 3
# 5
# 8
# 13
# -1
# >> 22
##########################################
x = int(input("Enter input: s"))
i = 0
a0 = 0
a1 = 1
while True:
    summ = a0 + a1
    a0 = a1
    a1 = summ
    print(summ)
    i += 1
    if i == 5:
        break
