# x = input()
# s = x.strip()
# ls = s.split(',')
# ss = ''
# for i in ls:
#     ss = ss + '"'
#     i1 = i.strip()
#     ss = ss + i1
#     ss = ss + '"'
#     ss = ss + ','
# sss = ss.rstrip(',')
# print(sss)

s = input()
b = s.strip()
w = '"'
c = ', '
for i in b:
    if i == ',' or c in w:
        w = w.strip()
    w += i
t = w.replace(',','","')
print('%s"'%t)
