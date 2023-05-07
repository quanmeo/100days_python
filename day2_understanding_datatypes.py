print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
num_of_people = int(input('How many people to split the bill? '))
tip = float(input('What percentage tip would you like to give? 10, 12, oe 15? '))
total_bill_plus_tip = total_bill * (1 + tip / 100)
money_each_person = total_bill_plus_tip / num_of_people
print(f'Each person should pay: ${money_each_person:.1f}\n')
