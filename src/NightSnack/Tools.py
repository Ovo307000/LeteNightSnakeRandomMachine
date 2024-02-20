import os
import subprocess
import webbrowser
import Setting

from tqdm import tqdm


def reset_color():
    return "\u001b[0m"


def exit_wait():
    input('Press Enter to exit...')


def GenshinImpart_start():
    for _ in range(1):
        if Setting.Config().get_config()["GenshinImpactPath"]:
            subprocess.Popen(Setting.Config().get_config()["GenshinImpactPath"], shell=True)
            break

        else:
            Setting.Config().change_config(key="GenshinImpactPath", value=get_GenshinImpart_path())
            GenshinImpart_start()


def finding_GenshinImpact():
    if Setting.Config().get_config()["openGenshinImpactUrl"]:
        print("你还没安装原神？")
        print("没关系！现在玩云原神！")

        open_url(Setting.Config().get_config().get("cloudGenshinImpactUrl"))


def not_found_GenshinImpact():
    if Setting.Config().get_config()["openGenshinImpactUrl"]:
        print("什么？你居然不玩原神？")

        open_url(Setting.Config().get_config().get("GenshinImpactUrl"))


def open_url(url):
    webbrowser.open(url)


def get_available_drives():
    return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":" + os.sep)]


def get_GenshinImpart_path():
    fileName = Setting.Config().get_config().get("GenshinImpactName")
    for path in get_available_drives():
        for root, dirs, files in tqdm(os.walk(path), desc="Searching game path..."):
            for name in fileName:
                if name in files:
                    print(f"Found {name} in {root}!")
                    filePath = os.path.join(root, name)
                    Setting.Config().change_config(key="GenshinImpactPath", value=filePath)
                    return Setting.Config().get_config()["GenshinImpactPath"]

        print(f"\nNot found {fileName} in {path}... \nSearching next drive...")

    return None
