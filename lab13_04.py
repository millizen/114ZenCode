startday = input().split("-")
endday = input().split("-")
sunday = int(input())

if endday[1] < startday[1]:
    temp = startday[:]
    startday = endday[:]
    endday = temp[:]

day1,day2 = int(startday[0]),int(endday[0])
month1,month2 = int(startday[1]),int(endday[1])
year = [31,28,31,30,31,30,31,31,30,31,30,31]
check = True
if month1 > 12 or month2 > 12:
    print("Wrong Month")
    month1,month2  = 1,1
    check = False
if sunday > 31 or day1 > year[month1-1] or day2 > year[month2-1]:
    print("Wrong Day")
    check = False
if check != False:
    count = 0
    if month1 == month2:
        if day1 > day2:
            temp = day1
            day1 = day2
            day2 = temp
    for i in range(sunday,sum(year[:month2-1]) + day2+1 ,7):
        if i >= sum(year[:month1-1]) + day1 and i <= sum(year[:month2]) + day2:
            count+=1
    print(count)
