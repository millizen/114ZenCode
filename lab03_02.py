amount_buy = float(input('Enter buying amount: '))
if(amount_buy > 1000 and amount_buy < 3000):
    amount_buy = amount_buy * (90/100)
elif(amount_buy > 3000):
    amount_buy = amount_buy * (85/100)
print('Amount due after discount is %.2f baht.' %amount_buy)
