def check_order(l):
    k = []
    k1 = []
    for i in l:
        k.append(i)
    for i in l:
        k1.append(i)
    la = []
    la1 = []
    k.sort()
    k1.sort(reverse = True)

    for i in range(len(l)):
        la.append(1)
    for i in l:
        la1.append(i/l[0])
    if len(l) == 0:
        a = "The list is empty."
    elif la == la1:
        a = "The list is in non-increasing and non-decreasing order."
    else:
        if l == k:
            a = "The list is in non-decreasing order."
        elif l == k1:
            a = "The list is in non-increasing order."
        elif l != k and l != k1:
            a = "The list is in random order."
    return a


l = []
while True:
    num = int(input("Enter a number (-1 to end): "))
    if num == -1:
        break
    elif num < 0 or num > 100:
        print("Number is out of range.")
    else:
        l.append(num)

print("-----\nOriginal list:")
print(l)
print(check_order(l))
