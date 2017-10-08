s = input()
day = int(input())
if s != "Sunday" and s != "Monday" and s != "Tuesday" and s != "Wednesday" and s != "Thursday" and s != "Friday" and s != "Saturday" or day <= 0 or day > 31 :
    print("ERROR")
else:
    print("9999")
