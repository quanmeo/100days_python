from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
coffee = CoffeeMaker()
menuu = Menu()

while True:
        items = menuu.get_items()
        command = input(f'What would you like ({items}): ')
        if command == 'report':
            coffee.report()
            machine.report()
        elif command == 'off':
            break
        elif command in ['latte', 'espresso', 'cappuccino']:
            item = menuu.find_drink(command)
            if item != None:
                if coffee.is_resource_sufficient(item):
                    if machine.make_payment(item.cost):
                        coffee.make_coffee(item)

