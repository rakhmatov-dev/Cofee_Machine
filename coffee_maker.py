from prettytable import PrettyTable


class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self, money_machine, in_pretty_table_format):
        """Prints report of all resources"""
        if not in_pretty_table_format:
            print(f"Water: {self.resources['water']}ml")
            print(f"Milk: {self.resources['milk']}ml")
            print(f"Coffee: {self.resources['coffee']}g")
        else:
            table = PrettyTable()
            table.title = "REPORT"
            table.add_column("Recourse", ["Water", "Milk", "Coffee", "Money"])
            table.add_column("Stocks", [f"{self.resources['water']}ml", f"{self.resources['milk']}ml", f"{self.resources['coffee']}g", f"{money_machine.CURRENCY}{money_machine.profit}"])
            # table.add_rows(
            #     [
            #         ["Water", f"{self.resources['water']}ml"],
            #         ["Milk", f"{self.resources['milk']}ml"],
            #         ["Coffee", f"{self.resources['coffee']}g"],
            #         ["Money", f"{money_machine.CURRENCY}{money_machine.profit}"]
            #     ]
            # )
            print(table)

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")
