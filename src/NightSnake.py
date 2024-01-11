# -*- coding: utf-8 -*-
# Build: python 3.12.0

import random
import os


class NightSnake:

    def __init__(self):
        self.nightSnakeStatement = [
            "今晚吃夜宵喵~",
            "今晚不吃夜宵喵~"
        ]

    def getRandomStatement(self):
        return random.choice(self.nightSnakeStatement)

    def printStatement(self):
        result = self.getRandomStatement()

        if result == self.nightSnakeStatement[0]:
            print("\u001b[32m" + result + "\u001b[0m")

        elif result == self.nightSnakeStatement[1]:
            print("\u001b[31m" + result + "\u001b[0m")


if (__name__ == '__main__'):
    NightSnake().printStatement()
    os.system("pause")
