import math
def circle(r1):
    return math.pi * r1 * r1
def circumference(r2):
    return math.pi * 2 * r2
def sphere(r3):
    return math.pi * (4/3) * (r3**3)

r = float(input("Enter a radius: "))
print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))
