import ast
ls = ast.literal_eval(input())
s = ''

for i in ls:
    s = s + i + ', '
s = s.strip(', ')
ss = ''
for i in range(len(s)-1,-1,-1):
    ss = ss + s[i]
ss = ss.replace(' ,',' & ',1)
for i in range(len(ss)-1,-1,-1):
    print(ss[i],end='')
