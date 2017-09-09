a = int(input("Enter your age: "))
if a>=15 and a<=60:
    m = int(input("Enter your net income: "))
    if m>=1 or m<=79999:
        if m>=1 and m<=30000:
            ans = (m*20)/100
            print("Your negative income tax is %.2f Baht." %ans)
        elif m>30000 and m<=79999:
            ans = 6000 - ((m-30000)*12)/100
            print("Your negative income tax is %.2f Baht." %ans)
        else:
            print("Invalid income.")
else:
    m = int(input('Enter your net income: '))
    print("Invalid age.")
