import random


def getRandomNumber():
    return random.randint(0, 1)


def checkNumber(number):
    if number == 0:
        return "今晚夜宵喵！"
    elif number == 1:
        return "今晚没有夜宵喵！"


if __name__ == '__main__':
    number = getRandomNumber()

    print(checkNumber(number))
