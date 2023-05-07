rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random as rd

ascii_dict = {0: rock, 1: paper, 2: scissors}

user = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer = rd.choice(range(3))

print('You choose')
print(ascii_dict[user])
print('Computer choose')
print(ascii_dict[computer])

if user == computer:
    print('Draw')
elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
    print('You win!')
else:
    print('You lose')
