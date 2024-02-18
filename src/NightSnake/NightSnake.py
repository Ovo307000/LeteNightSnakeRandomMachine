import random

from src.NightSnake import Tools, Setting

canEatStr = "今晚吃夜宵喵~"
cannotEatStr = "今晚不吃夜宵喵~"
result = ""

Statement = {
    canEatStr: "\u001b[32m",
    cannotEatStr: "\u001b[31m"
}


def getRandomStatement():
    return random.choice(list(Statement.keys()))


def getStatementColor(statement):
    return Statement[statement]


def statementCheck(statement):
    if statement == canEatStr:
        return False
    else:
        return True


def printStatement():
    result = getRandomStatement()

    if statementCheck(result):
        canEat()
    else:
        cannotEat()


def canEat():
    print(getStatementColor(canEatStr) + canEatStr + Tools.resetColor())


def cannotEat():
    if Setting.currentConfig["GenshinImpactStart"]:
        Tools.GenshinImpartStart(Tools.getGenshinImpartPath())

    print(getStatementColor(cannotEatStr) + cannotEatStr + Tools.resetColor())
