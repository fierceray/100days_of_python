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
    "milk": 300,
    "coffee": 100,
    "money": 0,
}

# return the resources.
def get_resource():
    return resources

# take parameter of resource dict and update the resources.
def set_resource(res):
    for item in resources:
        resources[item] = res[item]

def report():
    res = get_resource()
    print(f"Water: {res['water']}ml\n"
          f"Milk: {res['milk']}ml\n"
          f"Coffee: {res['coffee']}g\n"
          f"money: {res['money']}")

def check_enough_resource(coffee):
    # Check if there is enough resource
    required_igd = MENU[coffee]['ingredients']
    res = get_resource()
    prompt_string = ''
    is_enough = True
    for igd in required_igd:
        if required_igd[igd] > res[igd]:
            if '' == prompt_string:
                prompt_string += igd
            else:
                prompt_string += " and " + igd
            is_enough = False

    if is_enough:
        return True
    else:
        print("Sorry there is not enough {}.".format(prompt_string))
        return False


# Process coin
def process_coin():
    # input coins and return total amount
    print("Please insert coins.")
    coins = {
        'quarters': 0.25,
        'dimes': 0.1,
        'nickles': 0.05,
        'pennies': 0.01,
             }
    total = 0
    for coin in coins:
        total += coins[coin] * int(input(f'How many {coin}? '))

    print('You put total amount : {:.2f}'.format(total))

    return total

def check_transaction(coffee, money_in):
    # if more then give change, and process the resource accordingly
    # if less then prompt user not enough money
    cost = MENU[coffee]['cost']
    if money_in < cost:
        print("Sorry that's not enough money. Money refunded.")
    else:
        if money_in > cost:
            print(f"Here is ${(money_in - cost):.2f} in change.")

        # Make the coffee and deduce the resource and add the money
        res = get_resource()
        for igd in MENU[coffee]['ingredients']:
            res[igd] -= MENU[coffee]['ingredients'][igd]
        res['money'] += cost
        # Update the resources
        set_resource(res)
        print(f'Here is your {coffee}, enjoy!')

while True:
    # prompt "what you need"
    user_select_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    # End the program when input "off"
    if 'off' == user_select_coffee:
        print("Power off, goodbye!")
        break
    # print report when input "report"
    elif 'report' == user_select_coffee:
        # report print
        report()
    elif user_select_coffee in MENU:
        print('You selected {}.'.format(user_select_coffee))
        if check_enough_resource(user_select_coffee):
            # enough resource, prompt to input coin
            money_in = process_coin()
            check_transaction(user_select_coffee, money_in)
        else:
            #not enough resource
            continue
    else:
        print("Incorrect input, please try again.")