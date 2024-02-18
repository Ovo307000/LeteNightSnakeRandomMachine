import os
import Setting


def resetColor():
    return "\u001b[0m"


def exitWait():
    input("Press Enter to continue...")


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def GenshinImpartStart(paths):
    if not paths:
        print("什么？你居然不玩原神？")
        return

    for path in paths:
        os.system(fr"'{path}'")


def getAvailableDrives():
    return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]


def findFile(fileName, simplePath, fullPath=None):
    if fullPath:
        for root, dirs, files in os.walk(simplePath + "\\"):
            if fileName in files:
                return os.path.join(root, fileName)
        return None

    else:
        for root, dirs, files in os.walk(simplePath + "\\"):
            if fileName in files:
                return os.path.join(root, fileName)
    return None


def getGenshinImpartPath():
    fileName = ["YuanShen.exe", "GenshinImpact.exe"]

    for path in getAvailableDrives():
        for name in fileName:
            filePath = findFile(name, path)
            if filePath:
                return filePath.replace("\\", "\\\\")
    return None


def systemCheck():
    if os.name == "nt":
        return Setting.getCurrentConfig().get("Windows")
    else:
        return Setting.getCurrentConfig().get("otherOS")
