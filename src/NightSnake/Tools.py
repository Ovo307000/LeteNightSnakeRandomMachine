import os


def resetColor():
    return "\u001b[0m"


def exitWait():
    input("Press Enter to continue...")


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def GenshinImpartStart(path):
    if not path:
        print("什么？你居然不玩原神？")
        return

    os.system(path)
    print("原神! 启动!")


def getAvailableDrives():
    return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]


def findFile(fileName, simplePath):
    for root, dirs, files in os.walk(simplePath + "\\"):
        if fileName in files:
            return os.path.join(root, fileName)
    return None


def getGenshinImpartPath():
    fileName = ["YuanShen.exe", "GenshinImpact.exe"]

    for path in getAvailableDrives():
        filePath = findFile(fileName, path)
        if filePath:
            return filePath.replace("\\", "\\\\")
    return None
