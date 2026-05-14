MENU = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 60,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 80,
    },
}

resources = {
    "ingredients": {"water": 1000, "milk": 1000, "coffee": 100},
    "money": 0,
}

def check_availability(order, resources):
    for item in order['ingredients']:
        if order['ingredients'][item] > resources['ingredients'][item]:
            return "not_available"
    return "available"

is_on = True
while is_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("Shutting down. Goodbye!")
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['ingredients']['water']}ml")
        print(f"Milk: {resources['ingredients']['milk']}ml")
        print(f"Coffee: {resources['ingredients']['coffee']}g")
        print(f"Money: ₹{resources['money']}")

    elif choice in MENU:            # ✅ cleaner than or-chain
        order = MENU[choice]
        if check_availability(order, resources) == "not_available":
            print("Sorry, not enough ingredients for this order.")
        else:
            print(f"\nThe cost is ₹{order['cost']}. Insert money.")
            biggest = int(input("How many ₹100 notes: "))
            big = int(input("How many ₹50 notes: "))
            small = int(input("How many ₹20 notes: "))
            smallest = int(input("How many ₹10 notes: "))
            total_money = biggest*100 + big*50 + small*20 + smallest*10

            if total_money < order['cost']:
                print("That's not enough money. Order cancelled.")
            else:
                change = total_money - order['cost']
                if change > 0:
                    print(f"Here is your change of ₹{change}")
                print(f"Enjoy your {choice}! ☕")
                resources['money'] += order['cost']
                for item in order['ingredients']:
                    if order['ingredients'][item] > 0:   # ✅ skip zero
                        resources['ingredients'][item] -= order['ingredients'][item]

    else:
        print("Invalid choice. Please type espresso, latte, or cappuccino.")
