from data_base import MENU, resources, coffee_emoji

MONEY = 0


def print_report():
    """Prints report about current status of resources"""
    for key in resources:
        if key == "water" or key == "milk":
            print(f"{key.title()}: {resources[key]}ml")
        elif key == "coffee":
            print(f"{key.title()}: {resources[key]}g")
    print(f"Money: ${MONEY}")


def check_resources(menu_item):
    """Check if we have enough resources for user choice from Menu"""
    menu_item_ingredients = MENU[menu_item]["ingredients"]
    for key in menu_item_ingredients:
        if menu_item_ingredients[key] > resources[key]:
            print("Sorry there is not enough water.")
            return False
    return True


def change_resources(menu_item, menu_item_cost):
    """Change resources and money values"""
    global MONEY
    MONEY += menu_item_cost
    menu_item_ingredients = MENU[menu_item]["ingredients"]
    for key in resources:
        if key in menu_item_ingredients:
            resources[key] -= menu_item_ingredients[key]


def check_transaction(menu_item, quarters, dimes, nickles, pennies):
    """Check if user insert enough money"""
    menu_item_cost = MENU[menu_item]["cost"]
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if menu_item_cost > total:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if total > menu_item_cost:
            print(f"Here is ${round(total - menu_item_cost, 2)} dollars in change.")
        change_resources(menu_item, menu_item_cost)
        print(f"Here is your {menu_item} {coffee_emoji}. Enjoy!")


def coffee_machine():
    """Our Coffee Machine"""
    while True:
        # TODO: 1. Print Coffee Machine Logo
        # TODO: 2. Clear console
        users_wish = input("What would you like? (espresso/latte/cappuccino): ")
        if users_wish == "report":
            print_report()
        elif users_wish == "off":
            break
        else:
            if check_resources(users_wish):
                print("Please insert coins.")
                quarters = int(input("How many quarters? "))
                dimes = int(input("How many dimes? "))
                nickles = int(input("How many nickles? "))
                pennies = int(input("How many pennies? "))
                check_transaction(users_wish, quarters, dimes, nickles, pennies)


coffee_machine()
