summ = 0
while True:
    x = int(input("Enter a number: "))
    print(x)
    summ = summ + x
    if x == 0:
        print("End")
        break
print(summ)
