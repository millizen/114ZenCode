def simple_interest(p1, r1, t1):
    a = p1 + (((p1 * r1)/100) * t1)
    return a

def compound_interest(p2, r2, t2):
    b = p2 * ((1 + (r2/100))**t2)
    return b


p = float(input('Enter principle: '))
r = float(input('Enter interest rate: '))
t = float(input('Enter time: '))

print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))
