def accum_sum(l):
    ll = []
    summ = 0
    for i in l:
        summ += i
        ll.append(summ)
    return ll

li = []
while True:
    num = int(input('Enter a number (0 to end): '))
    if num < 0 or num > 999:
        print('Number is out of range.')
    elif num == 0:
        break
    else:
        li.append(num)
print('Original list:')
print(li)
print('Accumulative Sum:')
ll = accum_sum(li)
for i in ll:
    print(i)
