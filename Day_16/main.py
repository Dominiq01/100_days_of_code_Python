from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while is_on:
    user_input = input(f"What would you like? ({menu.get_items()}): ")

    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        resources_ok = coffee_machine.is_resource_sufficient(drink)
        if resources_ok:
            cost = drink.cost
            payment_accepted = money_machine.make_payment(cost)
            if payment_accepted:
                coffee_machine.make_coffee(drink)
