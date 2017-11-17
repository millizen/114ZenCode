s = input()
s = s.lower()
s = s.replace(' ','')
ls = []
ls1 = []
# print(len(s))
for i in range(len(s)-1):
    j = i + 2
    ls.append(s[i:j])
# print(ls)
ls.sort()
for i in ls:
    if i not in ls1:
        print(i)
    ls1.append(i)
