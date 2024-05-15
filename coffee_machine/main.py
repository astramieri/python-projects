import os
import art
import data


def select_product():
    products = "/".join(available_products())
    choice = input(f"What would you like? ({products}): ").lower()

    if choice == "off":
        return None
    elif choice in data.menu:
        product = data.menu[choice]
        print(f"You have selected: {choice.upper()}. Total cost: ${product['cost']}. Ingredients: {product['ingredients']}.")
    else:
        print("Product not found. Please, select a new product.")
        return select_product()

    return product


def insert_coins():
    coins = ", ".join(data.coins)
    print(f"Please insert coins. Accepted: {coins}.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    money = 0
    money += quarters * data.coins["Quarter"]
    money += dimes * data.coins["Dime"]
    money += nickels * data.coins["Nickel"]
    money += pennies * data.coins["Penny"]

    return round(money, 2)


def enough_money(money, product):
    if money < product["cost"]:
        return False
    else:
        return True


def available_products():
    available_products = []

    for product in data.menu:
        enough_resources = True

        ingredients = data.menu[product]["ingredients"]

        for ingredient in ingredients:
            if ingredients[ingredient] > data.resources[ingredient]:
                enough_resources = False
                break

        if enough_resources:
            available_products.append(product)

    return available_products


def start_machine():
    stop_machine = False
    total_money = 0

    os.system("cls")
    print(art.logo)

    while not stop_machine:
        print(f"Total money: {total_money}")
        print(f"Resources: {data.resources}")

        products = available_products()

        if len(products) == 0:
            print("No enough resources left. Please fill the machine.")
            print(f"Resources: {data.resources}")
            stop_machine = True
        else:
            product = select_product()

            if product is None:
                print("Machine turned off.")
                stop_machine = True
            else:
                money = insert_coins()

                if not enough_money(money, product):
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    total_money += round(product["cost"], 2)
                    extra = round(money - product["cost"], 2)

                    for key in product["ingredients"]:
                        data.resources[key] -= product["ingredients"][key]

                    if extra > 0:
                        print(f"Here is ${extra} dollars in change.")

                    print(f"Here is your beverage. Enjoy!")

        print("")

    print(f"Total money: ${total_money}")


start_machine()
