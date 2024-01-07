import random

canEat = "今晚吃夜宵喵~"
canNotEat = "今晚不吃夜宵喵~"

def getRandomNumber():
    return random.randint(0, 1)


def checkNumber(number):
    if number == 0:
        return True
    elif number == 1:
        return False


def printResult(result):
    if result == True:
        print(f"\u001b[32m {canEat} \u001b[0m")
    elif result == False:
        print(f"\u001b[31m {canNotEat} \u001b[0m")


def run():
    number = getRandomNumber()
    result = checkNumber(number)
    printResult(result)


if __name__ == '__main__':
    run()
