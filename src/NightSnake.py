# -*- coding: utf-8 -*-

import random


class NightSnake:

    def __init__(self):
        self.nightSnakeStatement = {
            "今晚吃夜宵喵~": "\u001b[32m",
            "今晚不吃夜宵喵~": "\u001b[31m"
        }

        self.colorReset = "\u001b[0m"

    def getRandomStatement(self):
        return random.choice(list(self.nightSnakeStatement.keys()))

    def colorCheck(self, statement):
        return self.nightSnakeStatement[statement] + statement + self.colorReset

    def printStatement(self):
        result = self.getRandomStatement()

        print(self.colorCheck(result))


if __name__ == '__main__':
    NightSnake().printStatement()

    input("Press Enter to continue...")