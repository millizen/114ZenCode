def digit(num):
    one = num % 10
    return one
def tens(num):
    a = num % 100
    two = a // 10
    return two
def hundreds(num):
    a = num % 1000
    three = a // 100
    return three
def thousands(num):
    a = num % 10000
    four = a // 1000
    return four
def sum_digits(num):
    a = num % 10
    b = (num % 100)//10
    c = (num % 1000)//100
    d = (num % 10000)//1000
    return a + b + c + d

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))
