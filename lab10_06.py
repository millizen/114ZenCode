x = input()
l = "aeiouAEIOU"
lenn = len(x)
index = 0
while True:
    if index >= lenn:
        break

    if x[index] not in l:
        print(x[index],end='')
        index += 1

    elif x[index] in l:
        # if index == (lenn - 1):
        if index == (lenn -1):
            print(x[index],end='')
            break
        if x[index + 1] == 'p':
            if x[index + 2] == x[index]:
                print(x[index],end='')
                index += 3
            else:
                print(x[index],end='')
                index += 1
        else:
            print(x[index],end='')
            index += 1
