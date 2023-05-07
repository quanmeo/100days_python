logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os

candidates = {}

while True:
    print(logo)
    print('Welcome to the secret auction program')
    name = input('What is your name? ')
    bid = float(input("What's your bid? $"))
    candidates[name] = bid
    command = input("Are there any other bidders? Type 'yes' or 'no'\n")
    os.system('clear')
    if command != 'yes':
        break

max_name = ''
max_bid = 0

for name, bid in candidates.items():
    if bid > max_bid:
        max_name = name
        max_bid = bid

print(f"The winner is {max_name} with a bid of ${max_bid}")
