x = input()
a = 'aeiouAEIOU'
count = 0
for i in a:
    for j in x:
        if j == i:
            count+= 1
print(count)
