################## CONSTANTS #####################
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 10,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 8,
    }
}


profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

################## FUNCTIONS #####################

def print_report(resources, profit):
    print(f"""Water: {resources["water"]} ml\n"""
          f"""Milk: {resources["milk"]} ml\n"""
          f"""Coffee: {resources["coffee"]} g\n"""
          f"""Money: {profit} PLN""")


def sufficient_supplies_check(resources, coffee):
    ingredients = MENU[coffee]["ingredients"]

    water_needed  = ingredients.get("water", 0)
    milk_needed   = ingredients.get("milk", 0)
    coffee_needed = ingredients.get("coffee", 0)
    
    if resources["water"] >= water_needed and resources["milk"] >= milk_needed and resources["coffee"] >= coffee_needed:
        resources["water"] -= water_needed
        resources["milk"] -= milk_needed
        resources["coffee"] -= coffee_needed
        sufficient_supplies = True
        return sufficient_supplies, resources
    else:
        if resources["water"] < water_needed:
            print("Sorry, there is not enough water.")
            sufficient_supplies = False
            return sufficient_supplies, resources
    
        if resources["milk"] < milk_needed:
            print("Sorry, there is not enough milk.")
            sufficient_supplies = False
            return sufficient_supplies, resources
    
        if resources["coffee"] < coffee_needed:
            print("Sorry, there is not enough coffee.")
            sufficient_supplies = False
            return sufficient_supplies, resources



def sufficient_funds_check(coins, coffee):
    cost = MENU[coffee]["cost"]
    
    zloty_0_5 = coins["50 gr"]
    zloty_1   = coins["1 zl"]
    zloty_2   = coins["2 zl"]
    zloty_5   = coins["5 zl"]
    funds = zloty_0_5*0.5 + zloty_1 + zloty_2*2 + zloty_5*5
    
    if funds >= cost:
        sufficient_funds = True
        change = funds - cost
        return sufficient_funds, cost, change

    else:
        print("Sorry that's not enough money. Money refunded.")
        sufficient_funds = False
        return sufficient_funds, cost, funds



def insert_coins():
    coins = {}
    print("Please insert coins.")
    coins["5 zl"]  = int(input("How many 5 zl?: "))
    coins["2 zl"]  = int(input("How many 2 zl?: "))
    coins["1 zl"]  = int(input("How many 1 zl?: "))
    coins["50 gr"] = int(input("How many 50 gr?: "))
    return coins



def single_coffee_preparation(resources, coffee, profit):
    sufficient_supplies, resources = sufficient_supplies_check(resources, coffee)
    coins = insert_coins()
    sufficient_funds, cost, change = sufficient_funds_check(coins, coffee)
    
    if sufficient_supplies == True and sufficient_funds == True:
        if change != 0:
            print(f"""Here is {change} zl in change.""")
        print(f"""Here is your {coffee}. Enjoy!""")
        profit += cost
        return profit


def coffee_machine_operation(resources, profit):
    shut_down = "no"
    while shut_down != "yes":
        request = input("What would you like? (espresso/latte/cappuccino): ")
        match request:
            case "espresso":
                profit += single_coffee_preparation(resources, request, profit)
            case "latte":
                profit += single_coffee_preparation(resources, request, profit)
            case "cappuccino":
                profit += single_coffee_preparation(resources, request, profit)
            case "report":
                print_report(resources, profit)
            case _:
                print("Choose an available option.")
        
        
#################### MAIN ########################
coffee_machine_operation(resources, profit)