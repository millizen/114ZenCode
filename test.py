print("---<< Main Menu >>---")
print("    <B>urger Meal")
print("    <C>hicken Meal")
print("    <P>asta Meal")
cm = input("Enter your choice: ")
if cm == 'B' or cm == 'b' :
    print("---<< Burger Sub Menu >>---")
    print("    <R>egular Burger")
    print("    <C>heese Burger")
    print("    <D>ouble Cheese Burger")
    cs = input("Enter your choice: ")
    if cs == 'R' or cs == 'r' :
        print("Your Regular Burger is 60 Baht.")
    elif cs == 'C' or cs == 'c' :
        print("Your Cheese Burger is 75 Baht.")
    elif cs == 'D' or cs == 'd' :
        print("Your Double cheese Burger is 90 Baht.")
    else :
        print("Invalid sub menu choice.")
elif cm == 'C' or cm =='c' :
    print("---<< Chicken Sub Menu >>---")
    print("    <F>ried Chicken")
    print("    <G>rilled Chicken")
    print("    <C>hef's Chicken")
    cs = input("Enter your choice: ")
    if cs == 'F' or cs == 'f' :
        print("Your Fried Chicken is 120 Baht.")
    elif cs == 'G' or cs == 'g' :
        print("Your Grilled Chicken is 150 Baht.")
    elif cs == 'C' or cs == 'c' :
        print("Your Chef's Chicken is 180 Baht.")
    else :
        print("Invalid sub menu choice.")
elif cm == 'P' or cm == 'p' :
    print("---<< Pasta Sub Menu >>---")
    print("    <S>paghetti de Italiano")
    print("    <L>asagna Supreme")
    print("    <M>acaroni Special")
    cs = input("Enter your choice: ")
    if cs == 'S' or cs == 's' :
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif cs == 'L' or cs == 'l' :
        print("Your Lasagna Supreme is 120 Baht.")
    elif cs == 'M' or cs == 'm' :
        print("Your Macaroni Special is 100 Baht.")
    else :
        print("Invalid sub menu choice.")
else :
    print("Invalid main menu choice.")
