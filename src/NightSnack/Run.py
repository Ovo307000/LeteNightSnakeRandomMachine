from NightSnack import Tools, Setting
from Console import Color
import random
import NightSnack

# 如果当前文件为主文件
if __name__ == '__main__':
    # 打印当前版本

    with Color() as color:
        color.rainbow_sin(f"Local version = {Setting.Config().get_default_config()['version']}\n"
                          f"If you want to change the config, find at {Setting.Config().config_file_path}",
                            0.1, random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

    # 打印语句
    NightSnack.print_statement()
    # 退出前等待，防止程序执行完毕后直接退出
    Tools.exit_wait()
