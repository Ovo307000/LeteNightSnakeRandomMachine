import os
import json
from Console import Color


class Config:
    def __init__(self):
        self.config = {
            # 版本信息
            "version": "1.4.0",
            # 配置文件夹名称
            "configFolderName": "NightSnackConfig",
            # 配置文件名称
            "configName": "NightSnackConfig.json",
            # 配置文件夹路径，默认为当前工作目录
            "configPath": os.getcwd(),
            # 国服原神路径
            "YuanShenPath": None,
            # 国际服原神路径
            # 暂无引用
            "GenshinImpactPath": None,
            # 是否启动原神
            "GenshinImpactStart": False,
            # 是否打开国服原神官网
            "openGenshinImpactUrl": False,
            # 是否打开云原神官网
            "openCloudGenshinImpactUrl": False,
            # 国服原神官网
            "GenshinImpactUrl": "https://ys.mihoyo.com/",
            # 云原神官网
            "cloudGenshinImpactUrl": "https://ys.mihoyo.com/cloud/?utm_source=default#/",
            # 启动次数
            "startTimes": 0,

            # 作者信息
            "Author": ["Copilot", "ChatGpt", "Ovo307000"],
            # 原神程序名称
            "GenshinImpactName": ["YuanShen.exe", "GenshinImpact.exe"],

            # 是否启用作弊
            "openCheat": {
                # 是否总是吃夜宵
                "alwaysEat": False,
                # 是否总是不吃夜宵
                "neverEat": False
            },

            # 状态信息
            "statement": {
                # 可以吃夜宵
                "canEatSnake": {
                    # 输出的字符串
                    "string": "今晚吃夜宵喵~",
                    # 输出为绿色
                    "color": "\u001b[32m"
                },
                # 不能吃夜宵
                "cannotEatSnake": {
                    # 输出的字符串
                    "string": "今晚不吃夜宵喵~",
                    # 输出为红色
                    "color": "\u001b[31m"
                },
            },

            # 帮助信息
            "HelpString": {
                # 如何修改配置文件
                "ChangeSetting": "You can Change the Config at " + os.path.join(os.getcwd(), "NightSnackConfig",
                                                                                "NightSnackConfig.json"),

                # 永远不要设置所有的作弊为True
                "Cheat": "Remember NEVER SET ALL TO TRUE",
            },
        }
        # 获取配置文件夹路径
        self.config_folder_path = os.path.join(self.config["configPath"], self.config["configFolderName"])

        # 获取配置文件路径
        self.config_file_path = os.path.join(self.config_folder_path, self.config["configName"])

        # 加载配置文件
        self.load_config()

    def load_config(self):
        # 如果配置文件夹不存在则创建
        if not os.path.exists(self.config_folder_path):
            os.makedirs(self.config_folder_path)
        # 如果配置文件不存在则创建
        if not os.path.exists(self.config_file_path):
            self.save_config(self.config)
        # 若配置文件与文件夹都存在则
        else:
            # 检查版本
            self.version_check()
            # 检查并更新配置
            self.check_and_update_config()
            # 检查作弊配置
            self.check_cheat_config()

            # 读取配置文件并覆盖默认配置
            with open(self.config_file_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)

    # 保存配置文件
    # config: 需要被保存的配置文件
    def save_config(self, config):
        # 如果配置文件夹不存在则创建
        if not os.path.exists(self.config_folder_path):
            os.makedirs(self.config_folder_path)
        with open(self.config_file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

    # 更新配置文件
    def update_config(self, key, value):
        local_config = self.get_local_config()

        local_config[key] = value
        self.save_config(local_config)

    # 重置配置文件
    def reset_config(self):
        self.save_config(self.get_default_config())

    # 检查配置文件版本键是否与默认配置文件版本键相同
    def version_check(self):
        # 尝试读取配置文件并检查版本
        try:
            # 若配置文件存在则检查版本
            if os.path.exists(self.config_file_path):
                # 获取本地配置文件
                local_config = self.get_local_config()
                # 若本地配置文件版本键与默认配置文件版本键不同则重置版本键
                if local_config.get("version") != self.config.get("version"):
                    # 输出版本不匹配的信息
                    with Color() as color:
                        color.cprint("Config version is not match, reset the config...", "RED", "BOLD")
                    # 重置版本键
                    self.update_config(key="version", value=self.config.get("version"))
        # 若json文件损坏则重置配置文件
        except json.JSONDecodeError:
            with Color() as color:
                color.cprint("Config file is broken, reset the config...", "RED", "BOLD")
            self.reset_config()

    # 检查作弊配置
    def check_cheat_config(self):
        # 获取本地配置文件
        local_config = self.get_local_config()

        # 如果总是吃夜宵和总是不吃夜宵同时为True
        if local_config.get("openCheat").get("alwaysEat") and local_config.get("openCheat").get("neverEat"):
            # 输出错误信息

            with Color() as color:
                color.cprint("AlwaysEat and NeverEat are both True, reset the cheat config to false...", "RED", "BOLD")
            # 重置作弊配置为False
            local_config["openCheat"]["alwaysEat"] = False
            local_config["openCheat"]["neverEat"] = False

            # 保存配置文件
            self.save_config(local_config)

    # 检查并更新配置文件
    def check_and_update_config(self):
        # 尝试读取配置文件并检查配置文件
        try:
            # 获取本地配置文件
            local_config = self.get_local_config()
            # 遍历默认配置文件，获取默认配置文件的键和值
            for key, value in self.config.items():
                # 若默认配置文件的键不在本地配置文件中则添加键和值到本地配置文件
                if key not in local_config:
                    # 输出未找到的键
                    with Color() as color:
                        color.cprint(f"Key: ", "YELLOW", "BOLD")
                        color.rainbow_sin(f"{key}", 0.1, 64, 64, 64)
                        color.cprint(f" not found, add to the config...", "YELLOW", "BOLD")
                    # 添加键和值到本地配置文件
                    local_config[key] = value
            # 保存本地配置文件
            self.save_config(local_config)
        # 若json文件损坏则重置配置文件
        except json.JSONDecodeError:
            with Color() as color:
                color.cprint("Config file is broken, reset the config...", "RED", "BOLD")
            self.reset_config()

    # 获取默认配置文件
    def get_default_config(self):
        self.update_config("startTimes", self.get_local_config().get("startTimes") + 1)
        return self.config

    # 获取本地配置文件
    def get_local_config(self):
        # 尝试读取配置文件并返回文件对象
        try:
            with open(self.config_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        # 若json文件损坏则恢复默认配置并返回默认配置
        except json.JSONDecodeError:
            with Color() as color:
                color.cprint("Config file is broken, reset the config...", "RED", "BOLD")
            self.reset_config()
            return self.get_default_config()
        # 若json文件丢失则恢复默认配置并返回默认配置
        except FileNotFoundError:
            with Color() as color:
                color.cprint("Config file is missing, reset the config...", "RED", "BOLD")
            self.reset_config()
            return self.get_default_config()


# 测试
if __name__ == '__main__':
    config = Config()
    print(config.get_default_config())
    print(config.get_local_config())
    print(config.get_local_config())
    config.reset_config()
    print(config.get_local_config())
    config.update_config("GenshinImpactPath", "test")
    print(config.get_local_config())
    config.version_check()
    print(config.get_local_config())
    config.check_and_update_config()
    print(config.get_local_config())
