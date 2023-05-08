logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import os
import random

cards = [i for i in range(1, 11)] + [10] * 3

def get_random_card():
    return random.choice(cards)

def calculate_sum(lists: list):
    if 1 in lists and sum(lists) <= 11:
        return sum(lists) + 10
    else:
        return sum(lists)

def dealer_run(dealer: list):
    while calculate_sum(dealer) < 21:
        if random.choice([False, True]):
            dealer.append(get_random_card())
        else:
            break

def check_result(user_sum, dealer_sum):
    if user_sum > 21:
        print("You went over. You lose 😭")
    elif dealer_sum > 21:
        print("Computer went over. You win")
    elif user_sum < dealer_sum:
        print("You lose 😭")
    elif user_sum > dealer_sum:
        print("You win")
    else:
        print("Push")

while True:
    yes_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if yes_no != 'y':
        break
    os.system('clear')
    print(logo)
    users = []
    dealer = []
    for _ in range(2):
        users.append(get_random_card())
    dealer.append(get_random_card())
    while True:
        print(f"\tYour cards: {users}, current score: {sum(users)}")
        print(f"\tComputer's first card: {dealer[0]}")
        if sum(users) >= 21:
            break
        yes_no = input("Type 'y' to get another card, type 'n' to pass: ")
        if yes_no != 'y':
            break
        users.append(get_random_card())

    dealer_run(dealer)
    user_sum = calculate_sum(users)
    dealer_sum = calculate_sum(dealer)

    print(f"\tYour final hand: {users}, final score: {user_sum}")
    print(f"\tComputer's final hand: {dealer}, final score: {dealer_sum}")
    check_result(user_sum, dealer_sum)
