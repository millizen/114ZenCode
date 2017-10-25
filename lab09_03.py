def nb_year(p0, percent, aug, p):
    a = int(p0 + (p0 * (percent / 100)) + aug)
    day = 1
    if a >= p:
         day = 1
    else:
        while True:
            day += 1
            a = int(a + (a * (percent / 100)) + aug)
            if a >= p:
                break
    return day



print( nb_year(1000, 2, 30, 1150) )
print( nb_year(1500000, 0.25, 1000, 2000000) )

# nb_year(p0, percent, aug, p)
