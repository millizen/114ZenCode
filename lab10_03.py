x = input()
ls = "aeiouAEIOU"
count = 0
for i in x:
    if i not in ls:
        print(i,end ='')
