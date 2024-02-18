import json
import os

defaultConfig = {
    "version": "1.3.1",
    "configFolderName": "NightSnackConfig",
    "configName": "NightSnackConfig.json",
    "configPath": os.getcwd(),
    "YuanShenPath": None,
    "GenshinImpactPath": None,
    "GenshinImpactStart": False,
    "openCheat": False,
    "WindowsName": "Windows",
    "otherOS": "Gnu/Linux or MacOS",

    "Statement": {
        "canEatSnake": [
            "今晚吃夜宵喵~",
            "\u001b[32m"
        ],
        "cannotEatSnake": [
            "今晚不吃夜宵喵~",
            "\u001b[31m"
        ]
    }
}

currentConfig = defaultConfig


def getCurrentConfig():
    if not os.path.exists(getConfigPath()):
        writeConfig(defaultConfig, getConfigPath())
    return readConfig(getConfigPath())


def getDefaultConfig():
    return defaultConfig


def getConfigPath():
    return os.path.join(getDefaultConfig()["configPath"], getDefaultConfig()["configName"])


def getConfigLocation():
    return os.path.join(getDefaultConfig()["configPath"], getDefaultConfig()["configFolderName"],
                        getDefaultConfig()["configName"])


def getConfigFolderLocation():
    return os.path.join(getDefaultConfig()["configPath"], getDefaultConfig()["configFolderName"])


def writeConfig(config, path):
    if not os.path.exists(path):
        makeConfigFolder()

    if not config:
        config = getDefaultConfig()

    with open(path, "w") as f:
        f.write(json.dumps(config, indent=2))


def readConfig(path):
    with open(path, "r") as f:
        return json.loads(f.read())


def fixConfig(config):
    fixed = {
        "count": 0,
        "config": config
    }

    for key, value in getDefaultConfig().items():
        if not getCurrentConfig().get(key):
            config[key] = value

            fixed["count"] += 1

    writeConfig(config, getConfigPath())

    return fixed


def resetConfig():
    writeConfig(getDefaultConfig(), getConfigLocation())


def makeConfigFolder():
    folderPath = getConfigFolderLocation()
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


def toWindowsPath(path):
    return path.replace("/", "\\")


if __name__ == "__main__":
    resetConfig()
    print(getCurrentConfig())
