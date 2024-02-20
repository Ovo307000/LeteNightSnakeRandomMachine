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
            self.save_config()
        else:
            with open(self.config_file_path, "r", encoding="utf-8") as f:
                self.config = json.load(f)

    def save_config(self):
        if not os.path.exists(self.config_folder_path):
            os.makedirs(self.config_folder_path)
        with open(self.config_file_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=2)

    def change_config(self, key, value):
        self.get_config()[key] = value
        self.save_config()

    def reset_config(self):
        self.save_config()

    def get_config(self):
        return self.config
