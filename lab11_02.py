x = input()
s = x.strip()
ls = s.split(',')
ss = ''
for i in ls:
    ss = ss + '"'
    i1 = i.strip()
    ss = ss + i1
    ss = ss + '"'
    ss = ss + ','
sss = ss.rstrip(',')
print(sss)
