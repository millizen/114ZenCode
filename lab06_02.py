target = 72
count = 0
while True:
    x = int(input("Enter your guess: "))
    if x == target:
        print('Congratulations, your guess is correct.')
        count += 1
        break
    if x < 0 or x > 100:
        count += 1
        print('Sorry, your guess is out of range.')
    elif x < target:
        count += 1
        print('Sorry, your guess is too low.')
    elif x > target:
        count += 1
        print('Sorry, your guess is too high.')
print('Total number of guesses is %d.'%count)
