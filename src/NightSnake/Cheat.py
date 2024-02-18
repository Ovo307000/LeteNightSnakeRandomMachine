from src.NightSnake import NightSnake


def alwaysEat():
    NightSnake.canEat()


def neverEat():
    NightSnake.cannotEat()


def menuChoice():
    print("  Cheat Menu")
    print("1. Always Eat")
    print("2. Never Eat")

    menu = {"1": NightSnake.canEat, "2": NightSnake.cannotEat}

    while True:
        choice = input("Enter your choice: ")

        if choice in menu:
            menu[choice]()
            break
        else:
            print("\u001b[31m" + "Invalid choice! Please enter again." + "\u001b[0m")
