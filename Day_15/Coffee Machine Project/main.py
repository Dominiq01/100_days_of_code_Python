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
coffe_machine_running = True
machine_money = 0

def insert_coins(drink_cost):
    print("Please insert coins.")

    user_quarters = int(input("how many quarters?: "))
    user_dimes = int(input("how many dimes?: "))
    user_nickles = int(input("how many nickles?: "))
    user_pennies = int(input("how many pennies?: "))
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    user_sum = user_quarters * 0.25 + user_dimes * 0.1 + user_nickles * 0.05 + user_pennies * 0.01

    if user_sum < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = user_sum - drink_cost
        print(f"Here is ${change} in change.")
        return True

def check_resources(drink_ingredients):

    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True



while coffe_machine_running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        coffe_machine_running = False
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml "
              f"\nCoffee: {resources["coffee"]}g\nMoney: ${machine_money}")
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        drink = MENU[user_input]
        resources_ok = check_resources(drink["ingredients"])
        if resources_ok:
            drink_cost = drink["cost"]
            enough_coins = insert_coins(drink_cost)

            if enough_coins:
                if user_input == "espresso":
                    resources["milk"] = resources["milk"]
                else:
                    resources["milk"] = resources["milk"] - drink["ingredients"]["milk"]

                resources["water"] = resources["water"] - drink["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - drink["ingredients"]["coffee"]

                machine_money += drink_cost
                print(f"Here is your {user_input} ☕️. Enjoy!")



# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):” DONE
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. DONE
# TODO: 3. When the user enters “report” to the prompt, a report should be generated that shows DONE
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO: 4. Check resources sufficient? DONE
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# TODO: 5.  Process coins. DONE
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# TODO: 6. Check transaction successful? DONE
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here
# TODO: 7. Make Coffee. DONE
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink