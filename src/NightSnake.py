# -*- coding: utf-8 -*-

import random
import sys
import os


class Tools:
    GenshinFilePath = '"G:\\Genshin Impact\\Genshin Impact Game\\YuanShen.exe"'

    @staticmethod
    def resetColor():
        return "\u001b[0m"

    @staticmethod
    def exitWait():
        input("Press Enter to continue...")

    @staticmethod
    def clearScreen():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def GenshinImpartStart():
        print("原神! 启动!")

        os.system(Tools.GenshinFilePath)


class NightSnake:

    def __init__(self):
        self.canEatStr = "今晚吃夜宵喵~"
        self.cannotEatStr = "今晚不吃夜宵喵~"
        self.colorReset = "\u001b[0m"
        self.result = ""

        self.nightSnakeStatement = {
            self.canEatStr: "\u001b[32m",
            self.cannotEatStr: "\u001b[31m"
        }

    def getRandomStatement(self):
        return random.choice(list(self.nightSnakeStatement.keys()))

    def getStatementColor(self, statement):
        return self.nightSnakeStatement[statement]

    def statementCheck(self, statement):
        if statement == self.cannotEatStr:
            return False
        else:
            return True

    def printStatement(self):
        self.result = self.getRandomStatement()

        if self.statementCheck(self.result):
            self.canEat()
        else:
            self.cannotEat()

    def canEat(self):
        print(self.getStatementColor(self.canEatStr) + self.canEatStr + self.colorReset)

    def cannotEat(self):
        print(self.getStatementColor(self.cannotEatStr) + self.cannotEatStr + self.colorReset)

        Tools.GenshinImpartStart()


class Cheat:
    def __init__(self):
        self.nightSnake = NightSnake()

    def alwaysEat(self):
        NightSnake().canEat()

    def neverEat(self):
        NightSnake().cannotEat()

    def menuChoice(self):
        print("1. Always Eat")
        print("2. Never Eat")

        try:
            choose = input("Enter your choice: ")
        except ValueError:
            print("Invalid input")
            Tools().clearScreen()
            self.menuChoice()

        if choose == "1":
            Tools().clearScreen()
            print(self.alwaysEat())
            Tools().exitWait()

        elif choose == "2":
            Tools().clearScreen()

            print(self.neverEat())
            Tools().GenshinImpartStart()

            Tools().exitWait()


if __name__ == '__main__':
    print("NightSnake Version 1.2.0")

    if "--cheat" in sys.argv:
        Cheat().menuChoice()
        sys.exit()

    NightSnake().printStatement()
    Tools().exitWait()
