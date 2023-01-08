QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
resources = {"water": 300,
             "milk": 200,
             "coffee": 100,
             }


def coins_cost(choose_drink, total):
    cost = {"espresso": 1.5,
            "Latte": 2.5,
            "Cappuccino": 3.0}
    if total > cost[choose_drink]:
        your_change = float(total) - cost[choose_drink]
        print(f'Drink ready. Here is your {choose_drink}\nYour change:{your_change}')
    elif total == cost[choose_drink]:
        print(f'Drink ready. Here is your {choose_drink}\nYour change:0')
    else:
        print("not enough money")


def drink_resources(choose_drink):
    MENU = {"espresso": {"ingredients": {"water": 50, "milk": 5, "coffee": 18, }, "cost": 1.5, },
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24, }, "cost": 2.5, },
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24, }, "cost": 3.0, }
            }
    # resources = {"water": 300,
    #              "milk": 200,
    #              "coffee": 100,
    #              }

    if choose_drink == "report":
        print(resources)
    else:
        drink = choose_drink
        water = resources["water"] - MENU[drink]["ingredients"]["water"]
        milk = resources["milk"] - MENU[drink]["ingredients"]["milk"]
        coffee = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]

        if MENU[drink]["ingredients"]["water"] <= resources["water"]:
            if MENU[drink]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[drink]["ingredients"]["coffee"] <= resources["coffee"]:
                    resources["water"] = water
                    resources["milk"] = milk
                    resources["coffee"] = coffee
                    return 0
                else:
                    return 1


def play_game():
    machine_working = True
    while machine_working:
        choose_drink = input("what would you like? (espresso/latte/cappuccino): ").lower()
        if choose_drink == "off":
            machine_working = False
        else:
            if choose_drink == "espresso" or "Latte" or "cappuccino" or "report":
                drink_value = drink_resources(choose_drink)
            if drink_value == 1:
                print("not enough resources")
            elif drink_value == 0:
                quarters = int(input("how many quarters: ")) * QUARTERS
                dimes = int(input("how many dimes: ")) * DIMES
                nickles = int(input("how many nickles: ")) * NICKLES
                pennies = int(input("how many pennies: ")) * PENNIES
                total = quarters + dimes + nickles + pennies
                coins_cost(choose_drink, total)


play_game()