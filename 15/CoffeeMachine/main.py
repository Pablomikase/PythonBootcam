MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

# Sección de variables
user_choise = ""
machine_turned_on = True
money = 0.0


# Sección de definión de variables
def ask_for_user_choise():
    global user_choise
    global machine_turned_on
    user_local_choise = input("¿Qué te gustaría tomar? (espresso, latte, cappuccino) --> ").lower()
    if user_local_choise == "espresso" or user_local_choise == "latte" or user_local_choise == "cappuccino":
        user_choise = user_local_choise
        return True
    elif user_local_choise == "report":
        print_report()
        return False
    elif user_local_choise == "off":
        machine_turned_on = False
        return False
    else:
        print("Opción no invalida...")
        ask_for_user_choise()


def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    global money
    print("------------ Printing Report ---------------")
    print(f"Water : {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")
    print("--------------------------------------------")


def are_there_enough_resources():
    global user_choise
    demanded_water = MENU[user_choise]["ingredients"]["water"]
    demanded_milk = MENU[user_choise]["ingredients"]["milk"]
    demanded_coffe = MENU[user_choise]["ingredients"]["coffee"]
    machine_water = resources["water"]
    machine_milk = resources["water"]
    machine_coffee = resources["water"]
    if machine_water < demanded_water:
        print("No hay suficiente Agua :(..")
        return False
    elif machine_milk < demanded_milk:
        print("No hay suficiente Leche :( ..")
        return False
    elif machine_coffee < demanded_coffe:
        print("No hay sificiente Café :( ..")
        return False
    else:
        return True


def get_user_selection_price():
    return MENU[user_choise]["cost"]


def process_coins():
    global money
    cuarters = float(input("Inserta la catidad de cuarters: "))
    dimes = float(input("Inserta la catidad de dimes: "))
    nickels = float(input("Inserta la catidad de nickles: "))
    pennies = float(input("Inserta la catidad de pennies: "))
    total_money_inserted = cuarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    product_price = get_user_selection_price()
    if total_money_inserted < product_price:
        print("El dinero ingresado es insuiciente D:. Devolviendo el dinero ingresado")
        return False
    else:
        money += product_price
        cambio = round(total_money_inserted - product_price)
        print(f"Ejecutando pedido, su cambio es {cambio}$")
        return True


def make_coffee():
    demanded_water = MENU[user_choise]["ingredients"]["water"]
    demanded_milk = MENU[user_choise]["ingredients"]["milk"]
    demanded_coffe = MENU[user_choise]["ingredients"]["coffee"]
    resources["water"] -= demanded_water
    resources["milk"] -= demanded_milk
    resources["coffee"] -= demanded_coffe
    print(f"Aquí tienes tu {user_choise}, que lo disfrutes :)")


def run_program():
    while machine_turned_on:
        if ask_for_user_choise():
            if are_there_enough_resources():
                if process_coins():
                    make_coffee()
    print("Hasta luego, apagando máquina...")


# Sección de ejecución
run_program()
