s = input()
lenn = len(s)
ls = ''
while True:
    x = input()
    ls = ls + x
    if x == '0':
        break

index = 0
while True:
    for j in ls:
        if j == '0':
            s = s.replace(s[index],'-')
        elif j == s[index]:
            s = s.replace(s[index],j)
            break
    index += 1
    if index == lenn:
        break
print(s)
