import os
import json


class Config:
    def __init__(self):
        self.config = {
            "version": "1.4.0",
            "configFolderName": "NightSnackConfig",
            "configName": "NightSnackConfig.json",
            "configPath": os.getcwd(),
            "YuanShenPath": None,
            "GenshinImpactPath": None,
            "GenshinImpactStart": False,
            "openGenshinImpactUrl": False,
            "openCloudGenshinImpactUrl": False,
            "GenshinImpactUrl": "https://ys.mihoyo.com/",
            "cloudGenshinImpactUrl": "https://ys.mihoyo.com/cloud/?utm_source=default#/",

            "Author": ["Copilot", "ChatGpt", "Ovo307000"],
            "GenshinImpactName": ["YuanShen.exe", "GenshinImpact.exe"],

            "openCheat": {
                "alwaysEat": False,
                "neverEat": False
            },

            "statement": {
                "canEatSnake": {
                    "string": "今晚吃夜宵喵~",
                    "color": "\u001b[32m"
                },
                "cannotEatSnake": {
                    "string": "今晚不吃夜宵喵~",
                    "color": "\u001b[31m"
                },
            },

            "HelpString": {
                "ChangeSetting": "You can Change the Config at " + os.path.join(os.getcwd(), "NightSnackConfig",
                                                                                "NightSnackConfig.json"),
                "Cheat": "Remember NEVER SET ALL TO TRUE",
            },
        }
        self.config_folder_path = os.path.join(self.config["configPath"], self.config["configFolderName"])
        self.config_file_path = os.path.join(self.config_folder_path, self.config["configName"])
        self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_folder_path):
            os.makedirs(self.config_folder_path)
        if not os.path.exists(self.config_file_path):
            self.save_config(self.config)
        else:
            self.version_check()
            self.check_and_update_config()

            with open(self.config_file_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)

    def save_config(self, config):
        if not os.path.exists(self.config_folder_path):
            os.makedirs(self.config_folder_path)
        with open(self.config_file_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=2)

    def change_config(self, key, value):
        local_config = self.get_config()

        for k in local_config.keys():
            local_config[key] = value

        self.save_config(local_config)

    def update_config(self, key, value):
        with open(self.config_file_path, "r", encoding="utf-8") as f:
            local_config = json.load(f)

        local_config[key] = value
        self.save_config(local_config)

    def reset_config(self):
        self.save_config(self.config)

    def version_check(self):
        try:
            if os.path.exists(self.config_file_path):
                with open(self.config_file_path, "r", encoding="utf-8") as f:
                    local_config = json.load(f)
                if local_config.get("version") != self.config.get("version"):
                    print("Config version is not match, reset the config version...")
                    self.update_config(key="version", value=self.config.get("version"))
        except json.JSONDecodeError:
            print("Config file is broken, reset the config...")
            self.reset_config()

    def check_and_update_config(self):
        try:
            with open(self.config_file_path, "r", encoding="utf-8") as f:
                local_config = json.load(f)

            for key, value in self.config.items():
                if key not in local_config:
                    print(f"Config key {key} is not found, add the key to the config...")
                    local_config[key] = value

            self.save_config(local_config)

        except json.JSONDecodeError:
            print("Config file is broken, reset the config...")
            self.reset_config()

    def get_config(self):
        return self.config
