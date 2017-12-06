l = [1,1,2,3,4,5,7]
k = []
k1 = []
for i in l:
    k.append(i)
for i in l:
    k1.append(i)
k.sort()
k1.sort(reverse = True)
print(l)
print(k)
print(k1)
if l == k:
    print("The list is in non-decreasing order.")
if l == k1:
    print("The list is in non-increasing order.")
if l != k or l != k1:
    print("The list is in random order.")
