import os
import Setting
import subprocess

from tqdm import tqdm


def reset_color():
    return "\u001b[0m"


def exit_wait():
    input('Press Enter to exit...')


def GenshinImpart_start():
    for _ in range(1):
        if Setting.Config().get_config()["GenshinImpactPath"]:
            subprocess.Popen(Setting.Config().get_config()["GenshinImpactPath"], shell=True)
        else:
            Setting.Config().change_config(key="GenshinImpactPath", value=get_GenshinImpart_path())
            GenshinImpart_start()


def get_available_drives():
    return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":")]


def find_file(fileName, simplePath, fullPath=None):
    if fullPath:
        for root, dirs, files in tqdm(os.walk(fullPath), desc="Searching game path..."):
            if fileName in files:
                return os.path.join(root, fileName)

    else:
        for root, dirs, files in tqdm(os.walk(simplePath), desc="Searching game path..."):
            if fileName in files:
                return os.path.join(root, fileName)

    return None


def get_GenshinImpart_path():
    fileName = Setting.Config().get_config().get("GenshinImpactName")
    for path in get_available_drives():
        for name in fileName:
            filePath = find_file(name, path)

            print(f"Not found game in {path}... \n Searching next drive...")

            if filePath:
                print(f"Found game in {path}! Saving path...")

                Setting.Config().change_config(key="GenshinImpactPath", value=filePath)
                return Setting.Config().get_config()["GenshinImpactPath"]

    return None
