# -*- coding: utf-8 -*-

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

    def colorCheck(self, statement):
        if statement == self.nightSnakeStatement[0]:
            return "\u001b[32m" + statement + "\u001b[0m"

        elif statement == self.nightSnakeStatement[1]:
            return "\u001b[31m" + statement + "\u001b[0m"

    def printStatement(self):
        result = self.getRandomStatement()

        print(self.colorCheck(result))


if __name__ == '__main__':
    NightSnake().printStatement()
    os.system("pause")
