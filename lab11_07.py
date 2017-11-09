w = input()
a = w.replace('-',' ')
b = a.replace('_',' ')
c = b.replace('=',' ')
d = c.replace('.',' ')
e = d.replace('$',' ')
f = e.title()
g = f.replace(' ','')
count = 1
for i in g:
    if count == 1:
        print(i.lower(),end='')
        count+= 1
    else:
        print(i,end='')
