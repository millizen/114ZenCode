x = input()
strr = '\\/ *:|"<>.'
peIndex = x.rfind('.')
# print(peIndex)
if peIndex == -1:
    for i in x[:15]:
        if i in strr:
            print('_',end='')
        else:
            print(i,end='')

elif peIndex > 15:
    for i in x[:15]:
        if i in strr:
            print('_',end='')
        else:
            print(i,end='')
    print('.',end='')
    for i in x[peIndex+1 : peIndex+4]:
        if i in strr:
            print('_',end='')
        else:
            print(i,end='')

elif peIndex <= 15:
    for i in x[:peIndex]:
        if i in strr:
            print('_',end='')
        else:
            print(i,end='')
    print('.',end='')
    for i in x[peIndex+1 : peIndex+4]:
        if i in strr:
            print('_',end='')
        else:
            print(i,end='')
