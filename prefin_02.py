a = 'aeiou'
x1 = input()
s = ''
x2 = input()
count1 = 1
for i in x1:
    if i in a:
        count1 += 1
    if count1 <= 2:
        s = s + i
cc = len(x2) - 1
boo = False
for i in x2:
    if i in a:
        boo = True
if boo:
    t = 0
    while t < len(x2):
        if x2[t] in a:
            index = t
            break
        t += 1
    count2 = 1
    s1 = ''
    while cc != index:
        s1 = s1 + x2[cc]
        cc -= 1
    ls = []
    cc1 = len(s1) - 1
    w = ''
    while cc1 != -1:
        w = w + s1[cc1]
        cc1 -= 1
else:
    w = x2
print(s + w)
