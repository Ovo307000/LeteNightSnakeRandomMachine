import sys

from src.NightSnake import NightSnake, Tools, Cheat

if __name__ == '__main__':
    print("NightSnake Version 1.3.1")

    if "--cheat" in sys.argv:
        Cheat.menuChoice()
        sys.exit()

    NightSnake.printStatement()
    Tools.exitWait()
