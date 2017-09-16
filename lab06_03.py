number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
    first = number1
    second = number2
elif number2 > number1:
    first = number2
    second = number1
elif number1 == number2:
    first = number1
    second = number2

while True:
    gcd = first % second
    first = second
    second = gcd
    if gcd == 0:
        break
lcm = (number1 * number2) / first
print("  >> gcd(%d, %d) = %6d" %(number1,number2,first))
print("  >> lcm(%d, %d) = %6d" %(number1,number2,lcm))
