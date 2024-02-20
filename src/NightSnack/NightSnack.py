import random

import Setting
import Tools


# 随机获取一条语句
def get_random_statement():
    # 返回随机选择的语句
    return random.choice(list(Setting.Config().get_default_config().get("statement").values()))


# 检查语句
def statement_check(statement):
    # 如果语句为可以吃夜宵
    if (statement.get("string") == Setting.Config().get_default_config()
            .get("statement")
            .get("canEatSnake")
            .get("string")):
        # 返回True
        return True
    # 如果语句为不可以吃夜宵
    elif (statement.get("string") == Setting.Config().get_default_config()
            .get("statement")
            .get("cannotEatSnake")
            .get("string")):
        # 返回False
        return False


# 打印语句
def print_statement():
    # 如果语句为True
    if statement_check(get_random_statement()):
        # 调用可以吃夜宵函数
        can_eat()
    # 如果语句为False
    else:
        # 调用不可以吃夜宵函数
        cannot_eat()


# 可以吃夜宵
def can_eat():
    # 打印可以吃夜宵的语句
    print(Setting.Config().get_default_config().get("statement").get("canEatSnake")["color"] +
          Setting.Config().get_default_config().get("statement").get("canEatSnake")["string"] + Tools.reset_color())


# 不可以吃夜宵
def cannot_eat():
    # 打印不可以吃夜宵的语句
    print(Setting.Config().get_default_config().get("statement").get("cannotEatSnake")["color"] +
          Setting.Config().get_default_config().get("statement").get("cannotEatSnake")["string"] + Tools.reset_color())

    # 如果配置文件中的openCheat为True
    if Setting.Config().get_default_config()["GenshinImpactStart"]:
        # 启动原神
        Tools.GenshinImpart_start()

    # 如果配置文件中的openGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openGenshinImpactUrl"]:
        # 打开原神官网
        Tools.open_GenshinImpact_web_page()

    # 如果配置文件中的openCloudGenshinImpactUrl为True
    if Setting.Config().get_default_config()["openCloudGenshinImpactUrl"]:
        # 启动云原神
        Tools.start_cloud_GenshinImpart()
