x = input()
a = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
for i in x:
    if i not in a:
        print(i,end='')
