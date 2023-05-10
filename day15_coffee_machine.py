MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

ingredient_list = ['water', 'milk', 'coffee']

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.1f}")

def enough(ingredient: str, ingredients: dict):
    if not ingredient in ingredients:
        return True

    return resources[ingredient] >= ingredients[ingredient]

def enough_resource(idx: int):
    if not idx in MENU:
        raise ValueError("Can't make this drink")
    drink = MENU[idx]['ingredients']

    for name in ingredient_list:
        if not enough(name, drink):
            print(f'Sorry there is not anough {name}')
            return False

    return True

def calculate(ingredient: str, ingredients: dict):
    resources[ingredient] -= 0 if ingredient in ingredients else ingredients[ingredient]


def calculate_resource(idx):
    if not idx in MENU:
        raise ValueError("Can't make this drink")
    ingredients = MENU[idx]['ingredients']

    [calculate(i, ingredients) for i in ingredient_list]
    global money
    money += MENU[idx]['cost']

def enough_money(idx: str):
    price = MENU[idx]['cost']

    print('Please insert coins.')
    quaters = int(input('how many quarters?: '))
    dimes = int(input('how many dimes?: '))
    nickles = int(input('how many nickles?: '))
    pennies = int(input('how many pennies?: '))

    total = quaters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${total} in change.")
        if total > price:
            print(f"Refund ${total - price}.")
        print(f"Here is your {idx}. Enjoy")

        return True

while True:
    command = input('What would you like? (espresso/latte/cappuccino): ')
    if command == 'report':
        print_report()
    elif command == 'off':
        break
    elif command in ['espresso', 'latte', 'cappucinno']:
        if enough_resource(command) and enough_money(command):
            calculate_resource(command)
    else:
        pass
