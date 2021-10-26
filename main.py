from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

options = menu.get_items(money_machine.CURRENCY, True)
print(f"{options}")
while is_on:
    choice = input("What would you like? ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report(money_machine, True)
        # money_machine.report()
    elif choice == "menu":
        print(f"{options}")
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_payment_successful:
            coffee_maker.make_coffee(drink)
