import os
import subprocess
import webbrowser
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
    config = Setting.Config().get_default_config()
    # 重试次数
    for _ in range(2):
        # 如果找到原神路径
        if config["GenshinImpactPath"]:
            with Color() as color:
                color.rainbow_sin(f"原神！！！启动！！！", 0.1, 0, 2, 4)
            # 使用subprocess启动原神，shell参数为True，则使用shell启动
            subprocess.Popen(config["GenshinImpactPath"], shell=True)
            # 退出当前循环
            return
        # 如果未找到原神路径
        else:
            # 获取原神路径
            config["GenshinImpactPath"] = get_GenshinImpart_path()
            Setting.Config().change_config(key="GenshinImpactPath", value=config["GenshinImpactPath"])


# 启动云原神
def start_cloud_GenshinImpart():
    # 如果配置文件中的openCloudGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openGenshinImpactUrl"]:
        with Color() as color:
            color.rainbow_sin(f"云原神！！！启动！！！", 0.1, 0, 2, 4)
        # 打开云原神官网
        open_url(Setting.Config().get_default_config().get("cloudGenshinImpactUrl"))


# 打开原神官网
def open_GenshinImpact_web_page():
    # 如果配置文件中的openGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openGenshinImpactUrl"]:
        with Color() as color:
            color.rainbow_sin(f"原神官网！！！启动！！！", 0.1, 0, 2, 4)
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
    fileName = Setting.Config().get_default_config().get("GenshinImpactName")
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
                    Setting.Config().change_config(key="GenshinImpactPath", value=filePath)
                    # 输出找到文件的信息
                    with Color() as color:
                        color.rainbow_sin(f"Find {fileName} in {filePath}!", 0.1, 0, 2, 4)

                    # 从配置文件中获取GenshinImpactPath键的值并返回
                    return Setting.Config().get_default_config()["GenshinImpactPath"]
        # 如果未找到指定文件，输出未找到文件的信息
        with Color() as color:
            color.cprint(f"Can't find {fileName} in {path}!", "RED", "BOLD")
    # 返回None
    return None
