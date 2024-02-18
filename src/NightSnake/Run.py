import sys
import json

from src.NightSnake import NightSnake, Tools, Cheat, Setting

if __name__ == '__main__':
    print("NightSnake Version 1.3.1")

    if "--startGame" in sys.argv:
        Setting.OpenGenshin = True

    if "--cheat" in sys.argv:
        Cheat.menuChoice()
        sys.exit()

    if "--help" in sys.argv:
        print(f"--startGame: Start Genshin Impact if the result is {NightSnake.cannotEatStr}")
        print( "    --cheat: Open the cheat menu")
        print( "     --help: Show this help message")

        Tools.exitWait()

    NightSnake.printStatement()
    Tools.exitWait()
