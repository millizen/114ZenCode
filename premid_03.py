day = int(input())
h = int(input())
mins = int(input())
if day > 7 or day <= 0 or h < 0 or h > 23 or mins < 0 or mins > 59:
    pass
else:
    if day == 1: d = "sunday.png"
    if day == 2: d = "monday.png"
    if day == 3: d = "tuesday.png"
    if day == 4: d = "wednesday.png"
    if day == 5: d = "thursday.png"
    if day == 6: d = "friday.png"
    if day == 7: d = "saturday.png"


    if  h >= 18 and h <= 22:
        if h == 18 and mins == 0:
            # print(55)
            r = "good-afternoon-"
        if h == 22 and mins > 0:
            # print(66)
            r = "good-night-"
        else : r = "good-evening-"
    if ((h == 22 and mins > 0) or h >= 23 or h == 0 or h == 1 or h == 2 or h == 3) or (h == 4 and mins == 0):
        # print(77)
        r = "good-night-"
    if h >= 12 and h <= 18:
        if h == 12 and mins == 0:
            # print(33)
            r = "good-morning-"
        if h == 18 and mins > 0:
            # print(44)
            r = "good-evening-"
        else : r = "good-afternoon-"
    if h >= 4 and h <= 12:
        # print(55)
        if h == 12 and mins > 0:
            # print("11")
            r = "good-afternoon-"
        if h == 4 and mins == 0:
            # print("22")
            r = "good-night-"
        else : r = "good-morning-"



print("%s%s"%(r, d))
