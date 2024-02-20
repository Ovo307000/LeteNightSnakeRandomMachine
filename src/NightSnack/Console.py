import math

import numpy as np


class Color:
    def __init__(self):
        self.color = {
            # 红色
            "RED": "\u001b[31m",
            # 绿色
            "GREEN": "\u001b[32m",
            # 黄色
            "YELLOW": "\u001b[33m",
            # 蓝色
            "BLUE": "\u001b[34m",
            # 品红
            "MAGENTA": "\u001b[35m",
            # 青色
            "CYAN": "\u001b[36m",
            # 白色
            "WHITE": "\u001b[37m"
        }

        self.style = {
            # 粗体
            "BOLD": "\u001b[1m",
            # 淡色
            "FAINT": "\u001b[2m",
            # 斜体
            "ITALIC": "\u001b[3m",
            # 下划线
            "UNDERLINE": "\u001b[4m",
            # 闪烁
            "REVERSE": "\u001b[7m",
            # 隐藏
            "HIDE": "\u001b[8m",
            # 删除线
            "STRIKETHROUGH": "\u001b[9m",
        }
        self.reset = "\u001b[0m"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.reset)

    # 采用sin函数生成彩虹字符串
    # string: 需要生成的字符串
    # step_rate: 步长，决定颜色的变化速度
    # start_red: 开始红色
    # start_green: 开始绿色
    # start_blue: 开始蓝色
    # end: 结尾，默认为空
    def rainbow_sin(self, string, step_rate, start_red, start_green, start_blue):
        for i in range(len(string)):
            print(f"\u001b[38;2;{int(math.sin(step_rate * i + start_red) * 127 + 128)};"
                  f"{int(math.sin(step_rate * i + start_green) * 127 + 128)};"
                  f"{int(math.sin(step_rate * i + start_blue) * 127 + 128)}m{string[i]}", end="")

    def rainbow_linear(self, string, start_color, end_color):
        r = np.linspace(start_color[0], end_color[0], len(string))
        g = np.linspace(start_color[1], end_color[1], len(string))
        b = np.linspace(start_color[2], end_color[2], len(string))

        for i in range(len(string)):
            print(f"\u001b[38;2;{int(r[i])};{int(g[i])};{int(b[i])}m{string[i]}", end="")

    def cprint(self, string, color, style=None):
        print(f"{self.color[color]}{self.style[style]}{string}{self.reset}")


if __name__ == '__main__':
    with Color() as color:
        color.rainbow_sin("Hello, World!", 0.1, 1, 2, 4)

        color.rainbow_linear("Hello, World!", (125, 125, 125), (255, 255, 255))

        color.cprint("Hello, World!", "RED", "BOLD")
