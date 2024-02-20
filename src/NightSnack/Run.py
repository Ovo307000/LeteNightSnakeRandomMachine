from NightSnack import Tools, Setting
import NightSnack

if __name__ == '__main__':
    print(f"Local version = {Setting.Config().get_config()["version"]}")
    print(f"If you want to change the config, please edit the config file in {Setting.Config().config_folder_path}")

    print(f"\n 夜宵时间到！")

    NightSnack.print_statement()
    Tools.exit_wait()
