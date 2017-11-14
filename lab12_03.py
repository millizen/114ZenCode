import math
ls = []
while True:
    x = float(input("Enter score: "))
    if x == -1:
        break
    if x < 0 or x > 100:
        print("Score is out of range.")
    else:
        ls.append(x)
# print(ls)
if len(ls) != 0:
    avg = sum(ls)/len(ls)
    su = 0
    for i in ls:
        a = (i - avg) ** 2
        su = su + a

    print("Maximum score is %.2f."%(max(ls)))
    print("Minimum score is %.2f."%(min(ls)))
    print("Average score is %.2f."%avg)
    print("Standard deviation is %.2f."%(math.sqrt(su/len(ls))))
