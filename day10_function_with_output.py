logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

import os

def calculate(first_num, second_num, command):
    ret = 1.0
    if command == '+':
        ret = first_num + second_num
    elif command == '-':
        ret = first_num - second_num
    elif command == '*':
        ret = first_num * second_num
    elif command == '/':
        ret = first_num / second_num

    print(f"{first_num} {command} {second_num} = {ret}")

    return ret

while True:
    print(logo)
    first_num = float(input("What's the first number?: "))

    [print(i) for i in list('+-*/')]
    while True:
        command = input('Pick an operation: ')
        second_num = float(input("What's the next number?: "))
        first_num = calculate(first_num, second_num, command)
        yes_no = input(f"Type 'y' to continue calculating with {first_num}, or type 'n' to start a new calculation: ")
        if yes_no != 'y':
            os.system('clear')
            break
