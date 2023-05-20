# Craete an application that will gives a 10% profit every 24hours

import datetime
import time

print('Welcome to Cohort 2 Asset management consult plc')

username = input('Enter your name: ')
amount = input('Enter Investment Amount: ')
print("Thanks", username, "for investing with us! Your Commission is underway")

time.sleep(1*30)

timenow = datetime.datetime.now()
td = datetime.timedelta(seconds=24 * 60 * 60)

def percentage_increase():
    user_amount = int(amount)
    total = user_amount * 0.10 + user_amount
    commission = user_amount * 0.10
    print(time.strftime("%c"))
    print('Your commssion is', commission)
    print(username,'congratulations your Capital is:',total)

    time.sleep(1*30)

 # While loop for infinite execution at every time.sleep(time)
    while True:
        timenow = td
        if timenow.seconds == 0 * 1 * 30:
            commission_roll = total * 0.1
            total = total * 1.1
            print(time.strftime("%c"))
            print('Your commssion after 24hrs is', int(commission_roll))
            print(username,'congratulations your New Capital after 24hrs is:',int(total))
        time.sleep(1*30)

percentage_increase()
