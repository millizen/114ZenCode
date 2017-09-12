minute = int(input("Minutes before due: "))
tem = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

day = minute // 1440

if minute % 1440 >= 720:
    day += 1

print(">>> %d days before due." % day)

if day < 2:
    print(">>> I will do the assignment.")
elif day > 5 or (tem > 40 or (tem > 25 and (rain == "Y" or rain == "y"))):
    print(">>> I will not do the assignment.")
else:
    print(">>> I will do the assignment.")
