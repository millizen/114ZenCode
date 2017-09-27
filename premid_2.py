print("Upper left corner coordinate:")
x = int(input("  << x axis: "))
y = int(input("  << y axis: "))
e = int(input("  << Eastern: "))
s = int(input("  << Southern: "))
print("Enter a coordinate:")
xn = int(input("  << x axis: "))
yn = int(input("  << y axis: "))

xx = x + e
yy = y - s
if (xn <= xx and xn >= x) and (yn >= yy and yn <= y):
    print("(%.2f, %.2f) is inside the rectangle."%(xn, yn))
else :
    print("(%.2f, %.2f) is not inside the rectangle."%(xn, yn))
