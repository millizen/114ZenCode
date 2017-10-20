x = input()
a = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
count = 0
for i in a:
    for j in x:
        if j == i:
            count+= 1
print(count)
