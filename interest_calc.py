"""
 Your loan
 Annual interest rate
 Monthly payment
 Nb of month

"""

loan = 50_000
annual_rate = 3
monthly = 1

monthly_rate = 3/100/12
owe = loan
count = 1
while owe > 0:
    count += 1
    interest = owe * monthly_rate
    owe = owe + interest - monthly
    if owe < monthly:
        print(f'your last payment on Month[{count}]: {owe}, of which {round(interest)} is the interest')
        break
    print(f'you own now ${round(owe)}, paid {monthly}, of which {round(interest)} is the interest')

