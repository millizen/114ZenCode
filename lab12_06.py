def remove_duplicates(t):
    ls = []
    for i in t:
        if i not in ls:
            ls.append(i)
    return ls


t = [1, 2, 3, 2, 1, 2, 3, 4]
print(remove_duplicates(t))
