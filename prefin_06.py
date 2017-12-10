# st = input()
# num = int(input())
# s = ''
# if num == 0 or num > len(st) or abs(num) > len(st) or len(st) == 0:
#     s = st
# elif num > 0:
#     l = len(st) - num
#     for j in range(l,len(st)):
#         s = s + st[j]
#     for i in range(l):
#         s = s + st[i]
# elif num < 0:
#     num = abs(num)
#     for j in range(num,len(st)):
#         s = s + st[j]
#     for i in range(num):
#         s = s + st[i]
# print(s)
s = input()
n = int(input())
y = abs(n)
if n!= 0:
    while y>len(s):
        y = y-len(s)
    if n>0:
        bot = s[:len(s)-y]
        top = s[len(s)-y:]
    else:
        top = s[y:]
        bot = s[:y]
    s = top+bot
print(s)
