x = input()
l = ['a', 'e', 'i', 'o', 'u']
lenn = len(x)
index = 0
while True:
    if x[index] not in l:
        print(x[index],end='')
        index += 1

    elif x[index] in l:
        print(x[index],end='')
        index += 3

    if index == lenn:
        break
