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


def getConfig():
    return defaultConfig


def getConfigPath():
    configName = currentConfig["configName"]
    configFolderName = currentConfig["configFolderName"]
    configPath = currentConfig["configPath"]

    return os.path.join(configPath, configFolderName, configName)


def writeConfig(configName, path):
    with open(path, "w") as f:
        f.write(json.dumps(configName, indent=2))


def readConfig(path):
    with open(path, "r") as f:
        return json.loads(f.read())


def refactorConfig(config):
    for key in defaultConfig:
        if key not in config:
            config[key] = defaultConfig[key]

    with open(getConfigPath(), "w") as f:
        f.write(json.dumps(config, indent=2))


def makeConfigFolder():
    folderPath = os.path.join(currentConfig["configPath"], currentConfig["ConfigFolderName"])

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)


def toWindowsPath(path):
    return path.replace("\\", "\\\\")

if '__main__' == __name__:
    print(toWindowsPath(getConfigPath()))
