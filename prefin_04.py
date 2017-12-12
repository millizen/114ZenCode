x = input()
s = ''
code = input()
dcode = input()
ls = []
x = x.replace(' ','')

for i in x:
    if i not in ls:
        s += i
        # print(i)
    ls.append(i)
# print(s)
if len(code) == len(s):
    for i in dcode:
        if i in code:
            print(s[code.find(i)],end='')
        else:
            print(i,end='')
