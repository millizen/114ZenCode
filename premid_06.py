x = int(input())
y = int(input())
z = int(input())

count = 0
if (x * x)+(y * y) == (z * z):
    count += 1
elif (y * y)+(z * z) == (x * x):
    count += 1
elif (z * z)+(x * x) == (y * y):
    count += 1
# print(count)
if count == 1:
    print("True")
elif count == 0 :
    print("False")
