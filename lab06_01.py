x = int(input('Enter a target (4-digit integer): '))
y = int(input('Enter your guess (4-digit integer): '))
div = 10
count = 4
r = 0
r1 = 0
while True:
    s = (x % div)
    a = s// (div/10)
    div = div * 10
    #print('==>%d'%a)
    # print('=>%d'%count)
    div1 = 10
    count1 = 4
    while True:
        s1 = (y % div1)
        a1 = s1// (div1/10)
        div1 = div1 * 10
        #print('%d'%a1)
        # print('*%d'%count1)
        if a == a1 :
            if count == count1:
                r +=1
            else:
                r1 += 1
        count1 -= 1
        if s1 == y :
            break
    count -= 1
    if s == x :
        break
# print('r =',r)
# print('r1 = ',r1)
if r == 0 :
    if r1 == 0:
        print('No positions correct, no digits correct')
    elif r1 == 1:
        print('No positions correct, one digit correct')
    elif r1 == 2:
        print('No positions correct, two digits correct')
    elif r1 == 3:
        print('No positions correct, three digits correct')
    elif r1 == 4:
        print('No positions correct, four digits correct')
elif r == 1 :
    if r1 == 0:
        print('One position correct, no digits correct')
    elif r1 == 1:
        print('One position correct, one digit correct')
    elif r1 == 2:
        print('One position correct, two digits correct')
    elif r1 == 3:
        print('One position correct, three digits correct')
    elif r1 == 4:
        print('One position correct, four digits correct')
elif r == 2 :
    if r1 == 0:
        print('Two positions correct, no digits correct')
    elif r1 == 1:
        print('Two positions correct, one digit correct')
    elif r1 == 2:
        print('Two positions correct, two digits correct')
    elif r1 == 3:
        print('Two positions correct, three digits correct')
    elif r1 == 4:
        print('Two positions correct, four digits correct')
elif r == 3 :
    if r1 == 0:
        print('Three positions correct, no digits correct')
    elif r1 == 1:
        print('Three positions correct, one digit correct')
    elif r1 == 2:
        print('Three positions correct, two digits correct')
    elif r1 == 3:
        print('Three positions correct, three digits correct')
    elif r1 == 4:
        print('Three positions correct, four digits correct')
elif r == 4 :
    if r1 == 0:
        print('Congratulations, you just mastered my mind!!')
    elif r1 == 1:
        print('Congratulations, you just mastered my mind!!')
    elif r1 == 2:
        print('Congratulations, you just mastered my mind!!')
    elif r1 == 3:
        print('Congratulations, you just mastered my mind!!')
    elif r1 == 4:
        print('Congratulations, you just mastered my mind!!')
