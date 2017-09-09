import math
x = float(input('Enter x : '))
if x<0:
    f1 = (x**2 + 1)**(1/2)
    print("f(%.2f) = %d" %(x, math.ceil(f1)))

elif x == 0:
    print('f(%.2f) = %d' %(x, x))

elif 0 < x <=99:
    f2 = 3*(x**2) - ((1-x)**2)
    print('f(%.2f) = %d' %(x, math.ceil(f2)))

else :
    f3 = 2*(x**3) - (x/((x+1)**(1/2)))
    print('f(%.2f) = %d' %(x , math.ceil(f3)))
    
