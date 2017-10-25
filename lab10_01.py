# num = int(input())
# a = num
# count = 0
# i = 1
# i1 = 1
# while True:
#     print('|',end='')
#     print(' ' * (a - i),end='')
#     print('*' * i1,end='')
#     print(' ' * (a - i),end='')
#     print('|')
#     i1 += 2
#     i += 1
#     count += 1
#     if count == num:
#         break
#________________________________________________________
num = int(input())
a = num
count = 0
i = 1
i1 = 1
while True:
    s = '|'
    s = s + (' ' * (a - i))
    s = s + ('*' * i1)
    s = s + (' ' * (a - i))
    s = s + '|'
    print(s)
    i1 += 2
    i += 1
    count += 1
    if count == num:
        break
