import sys

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

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def payment():
    print("Please insert coins.")
    payment = int(input("how many quarters?: ")) * 0.25
    payment += int(input("how many dimes?: ")) * 0.1
    payment += int(input("how many nickles?: ")) * 0.05
    payment += int(input("how many pennies?: ")) * 0.01
    return payment


def requirements(requirements):
    for item in requirements:
        if requirements[item] > requirements[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


state = True

while state:
    select = input("What would you like? (espresso/latte/cappuccino): ")

    if select == "off":
        select = False
        sys.exit()
    elif select == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU[select]
        if requirements(drink["ingredients"]):
            payment = payment()
            if transaction(payment, drink["cost"]):
                coffee(select, drink["ingredients"])