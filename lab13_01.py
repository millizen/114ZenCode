def namelist(ls):
    s = ''
    for i in ls:
        s = s + i + ', '
    s = s.strip(', ')
    ss = ''
    for i in range(len(s)-1,-1,-1):
        ss = ss + s[i]
    ss = ss.replace(' ,',' & ',1)
    sss = ''
    for i in range(len(ss)-1,-1,-1):
        sss = sss + ss[i]
    return sss




import ast
names = ast.literal_eval(input())
print( namelist(names) )
