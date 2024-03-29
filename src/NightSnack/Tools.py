import os
import subprocess
import webbrowser
import random
import Setting

from Console import Color
from tqdm import tqdm


# 重置控制台颜色
def reset_color():
    return "\u001b[0m"


# 退出时等待
def exit_wait():
    input('Press Enter to exit...')


# 启动原神
def GenshinImpart_start():
    game_path = Setting.Config().get_local_config().get("GenshinImpactPath")

    if not game_path or not os.path.exists(game_path):
        with Color() as color:
            color.cprint(f"Game path not found, start searching game path...", "RED", "BOLD")
        game_path = get_GenshinImpart_path()

    if game_path and os.path.exists(game_path):
        try:
            with Color() as color:
                color.rainbow_sin(f"原神！！！启动！！！", 0.1, random.randint(64, 255), random.randint(64, 255),
                                  random.randint(64, 255))
            subprocess.Popen(game_path, shell=True)
            return

        except Exception as e:
            with Color() as color:
                color.cprint(f"Failed to start the game due to error: {str(e)}", "RED", "BOLD")

    with Color() as color:
        color.cprint("Failed to start the game after retrying.", "RED", "BOLD")


# 启动云原神
def start_cloud_GenshinImpart():
    # 如果配置文件中的openCloudGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openGenshinImpactUrl"]:
        with Color() as color:
            color.rainbow_sin(f"云原神！！！启动！！！", 0.1, random.randint(64, 255), random.randint(64, 255),
                              random.randint(64, 255))
        # 打开云原神官网
        open_url(Setting.Config().get_default_config().get("cloudGenshinImpactUrl"))


# 打开原神官网
def open_GenshinImpact_web_page():
    # 如果配置文件中的openGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openGenshinImpactUrl"]:
        with Color() as color:
            color.rainbow_sin(f"原神官网！！！启动！！！", 0.1, random.randint(64, 255), random.randint(64, 255),
                              random.randint(64, 255))
        # 打开原神官网
        open_url(Setting.Config().get_default_config().get("GenshinImpactUrl"))


# 打开指定网页
# url: 需要打开的网页
def open_url(url):
    webbrowser.open(url)


# 获取可用驱动器
def get_available_drives():
    # 返回一个列表，列表中的元素为可用驱动器
    # chr(x) + ":" 为驱动器名
    # range(65, 91) 为A-Z的ASCII码
    # os.path.exists(chr(x) + ":" + os.sep) 判断驱动器是否存在
    # 如果存在则加入列表
    # os.sep为路径分隔符
    return [chr(x) + ":" for x in range(65, 91) if os.path.exists(chr(x) + ":" + os.sep)]


# 获取原神路径
def get_GenshinImpart_path():
    # 获取配置文件中的GenshinImpactName键的值
    fileName = Setting.Config().get_local_config().get("GenshinImpactName")
    # 遍历可用驱动器
    for path in get_available_drives():
        # os.walk(path) 遍历path路径下的所有文件夹
        # root: 当前文件夹路径
        # dirs: 当前文件夹下的文件夹
        # files: 当前文件夹下的文件
        # tqdm() 为进度条
        # desc="Searching game path..." 为进度条的描述
        for root, dirs, files in tqdm(os.walk(path), desc="Searching game path..."):
            # 遍历文件夹下的文件
            for name in fileName:
                # 如果文件夹下有指定文件
                if name in files:
                    # os.path.join(root, name) 为拼接路径
                    filePath = os.path.join(root, name)
                    # 修改配置文件中的GenshinImpactPath键的值，方便下次启动
                    Setting.Config().update_config(key="GenshinImpactPath", value=filePath)
                    # 输出找到文件的信息
                    with Color() as color:
                        color.rainbow_sin(f"Find {name} in {root}!", 0.1, 0, 2, 4)

                    # 从配置文件中获取GenshinImpactPath键的值并返回
                    return Setting.Config().get_local_config()["GenshinImpactPath"]
        # 如果未找到指定文件，输出未找到文件的信息
        with Color() as color:
            color.cprint(f"Can't find {fileName} in {path}!", "RED", "BOLD")
    # 返回None
    return None
