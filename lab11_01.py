x = input()
ls = 'aeiou'
for i in x:
    if i in ls:
        print(i.upper(),end='')
    else:
        print(i.lower(),end='')
