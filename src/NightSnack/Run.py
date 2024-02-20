from NightSnack import Tools, Setting
import NightSnack

# 如果当前文件为主文件
if __name__ == '__main__':
    # 打印当前版本
    print(f"Local version = {Setting.Config().get_default_config()["version"]}")
    # 打印配置文件路径与提示
    print(f"If you want to change the config, please edit the config file in {Setting.Config().config_folder_path}")

    print(f"\n 夜宵时间到！")

    # 打印语句
    NightSnack.print_statement()
    # 退出前等待，防止程序执行完毕后直接退出
    Tools.exit_wait()
