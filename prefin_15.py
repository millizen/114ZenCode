s = input()
s = s.lower()
a = ['for', 'and', 'with', 'of']
ls = s.split()
# print(ls)
for i in ls:
    if i in a:
        print(i,end=' ')
    elif i not in a:
        print(i.capitalize(),end=' ')
