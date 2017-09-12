print('---<< Main Menu >>---')
print('    <B>urger Meal')
print('    <C>hicken Meal')
print('    <P>asta Meal')
x = input('Enter your choice: ')
if x == 'B' or x == 'b':
    print('---<< Burger Sub Menu >>---')
    print('    <R>egular Burger')
    print('    <C>heese Burger')
    print('    <D>ouble Cheese Burger')
    y = input("Enter your choice: ")
    if y == 'r' or y == 'R':
        print('Your Regular Burger is 60 Baht.')
    elif y == 'C' or y == 'c':
        print('Your Cheese Berger is 75 Baht.')
    elif y == 'D' or y == 'd':
        print('Your Double Cheese Berger is 90 Baht.')
    else:
        print('Invalid sub menu choice.')
elif x == 'C' or x == 'c':
    print('---<< Chicken Sub Menu >>---')
    print('    <F>ried Chicken')
    print('    <G>rilled Chicken')
    print("    <C>hef's Chicken")
    e = input("Enter your choice: ")
    if e == 'F' or e == 'f':
        print('Your Fried Chicken is 120 Baht.')
    elif e == 'G' or e == 'g':
        print('Your Grilled Chicken is 150 Baht.')
    elif e == 'C' or e == 'c':
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print('Invalid sub menu choice.')
elif x == 'P' or x == 'p':
    print('---<< Pasta Sub Menu >>---')
    print('    <S>paghetti de Italiano')
    print('    <L>asagna Supreme')
    print('    <M>acaroni Special')
    p = input("Enter your choice: ")
    if p == 's' or p == 'S':
        print('Your Spaghetti de Italiano is 90 Baht.')
    elif p == 'L' or p == 'l':
        print('Your Lasagna Supreme is 120 Baht.')
    elif p == 'M' or p == 'm':
        print('Your Macaroni Special is 100 Baht.>')
    else:
        print('Invalid sub menu choice.')
else:
    print("Invalid main menu choice.")
