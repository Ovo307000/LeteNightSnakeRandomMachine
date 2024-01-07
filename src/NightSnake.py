import random

# 简易字符池
canEat = "今晚吃夜宵喵~"
canNotEat = "今晚不吃夜宵喵~"

# 通过随机数判断是否吃夜宵
def getRandomNumber():
    return random.randint(0, 1)


def checkNumber(number):
    if number == 0:
        return True
    elif number == 1:
        return False

# 打印结果
def printResult(result):
    if result == True:
        print(f"\u001b[32m {canEat} \u001b[0m")
    elif result == False:
        print(f"\u001b[31m {canNotEat} \u001b[0m")


# 将所有的函数组合起来，形成一个完整的程序
def run():
    number = getRandomNumber()
    result = checkNumber(number)
    printResult(result)


# 程序入口，调用run函数
if __name__ == '__main__':
    run()
