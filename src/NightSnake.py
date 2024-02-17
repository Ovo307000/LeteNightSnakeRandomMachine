# -*- coding: utf-8 -*-

import random
import sys
import os


class Tools:
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
    def GenshinImpartStart(path):
        print("原神! 启动!")

        os.system(path)

    @staticmethod
    def getAvailableDrives():
        return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]

    @staticmethod
    def findFile(fileName, simplePath):
        for root, dirs, files in os.walk(simplePath + "\\"):
            if fileName in files:
                return os.path.join(root, fileName)
        return None

    @staticmethod
    def getGenshinImpartPath():
        fileName = "YuanShen.exe"

        for path in Tools.getAvailableDrives():
            filePath = Tools.findFile(fileName, path)
            if filePath:
                # \033 为 \ 字符的转义字符
                return filePath.replace("\\", "\\\\")
        return None


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

        Tools.GenshinImpartStart(f"\"{Tools.getGenshinImpartPath()}\"")


class Cheat:
    def __init__(self):
        self.nightSnake = NightSnake()

    @staticmethod
    def alwaysEat():
        NightSnake().canEat()

    @staticmethod
    def neverEat():
        NightSnake().cannotEat()

    @staticmethod
    def menuChoice():
        print("  Cheat Menu")
        print("1. Always Eat")
        print("2. Never Eat")

        menu = {"1": NightSnake().canEat, "2": NightSnake().cannotEat}

        while True:
            choice = input("Enter your choice: ")

            if choice in menu:
                menu[choice]()
                break
            else:
                print("\u001b[31m" + "Invalid choice! Please enter again." + "\u001b[0m")


if __name__ == '__main__':
    print("NightSnake Version 1.2.3")

    if "--cheat" in sys.argv:
        Cheat().menuChoice()
        sys.exit()

    NightSnake().printStatement()
    Tools().exitWait()
