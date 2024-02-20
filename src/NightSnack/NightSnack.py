import random

from src.NightSnack import Tools, Setting


def get_random_statement():
    return random.choice(list(Setting.Config().get_config().get("statement").values()))


def statement_check(statement):
    if (statement.get("string") == Setting.Config().get_config()
            .get("statement")
            .get("canEatSnake")
            .get("string")):
        return True

    elif (statement.get("string") == Setting.Config().get_config()
            .get("statement")
            .get("cannotEatSnake")
            .get("string")):
        return False


def print_statement():
    result = get_random_statement()

    if statement_check(result):
        can_eat()
    else:
        cannot_eat()


def can_eat():
    print(Setting.Config().get_config().get("statement").get("canEatSnake")["color"] +
          Setting.Config().get_config().get("statement").get("canEatSnake")["string"] + Tools.reset_color())


def cannot_eat():
    print(Setting.Config().get_config().get("statement").get("cannotEatSnake")["color"] +
          Setting.Config().get_config().get("statement").get("cannotEatSnake")["string"] + Tools.reset_color())

    if Setting.Config().get_config()["GenshinImpactStart"]:
        Tools.GenshinImpart_start()
