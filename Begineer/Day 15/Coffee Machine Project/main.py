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
sales = 0

def stop():
    print("The machine will shutdown now...")
    return


def transaction(cost,profit):
    global sales
    sales +=profit
    for i in cost:
        resources[i] -= cost[i]
    prompt()




def report_resources(code):
    if code ==0:
        for i in resources:
            if i !="profit":
                print(f"{i}={resources[i]} ml")
        print(f"sales: ${sales}")
        prompt()
    else:
        values = []
        for i in resources:
            values.append(resources[i])

        return values

def coin_check(choice):
    Penny = float(input("How many Pennies ?"))*0.01
    Dime = float(input("How many Dime ?"))*0.10
    Nickel = float(input("How many nickels ?"))*0.05
    Quarter = float(input("How many quarters ?"))*0.25

    total_money = Penny + Dime + Nickel + Quarter

    if total_money < MENU[choice]['cost']:
        print("Sorry, that's not enough money . Money refunded")
        prompt()
    else:
        change = total_money - MENU[choice]['cost']
        print(f"Here is {change} \n Here is your {choice} ☕. Enjoy")
        profit = MENU[choice]['cost']
        return profit





def resource_check(choice):

    water,milk,coffee = report_resources(1)

    cost={}

    for i in MENU[choice]['ingredients']:
        cost[i]=(MENU[choice]['ingredients']).get(i)





    if water < cost['water'] :
        print("Insufficient water resources")
        prompt()
    if choice != "espresso":
        if milk < cost['milk'] :
            print("Insufficient milk resources")
            prompt()

    if coffee < cost['coffee'] :
        print("Insufficient coffee resources")
        prompt()

    profit = coin_check(choice)


    transaction(cost,profit)






# Todo : Recieve a prompt from the user

def prompt():
    user_input = (input("What would you like? (espresso, latte , cappuccino):")).lower()
    if user_input == "off":
        stop()
        return 0
    elif user_input == "report":
        report_resources(0)
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        resource_check(user_input)

    else:
        print("Please , choose any one of the given options")
        prompt()




prompt()