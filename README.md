# NightSnake
 一个随机决定是否来一个夜宵的小程序

## 介绍
这是一个随机决定是否来一个夜宵的小程序，可以用来解决夜宵的问题

## 使用说明
 - **构建版本**：
   - python 3.12.0
   - pyinstaller 6.3.0
   - pycharm 2023.2

## 类和方法

程序定义了一个名为`NightSnake`的类，该类包含以下方法：

- `__init__`：初始化方法，定义了一个名为`nightSnakeStatement`的列表，包含两个字符串，"今晚吃夜宵喵~"和"今晚不吃夜宵喵~"。
- `getRandomStatement`：从`nightSnakeStatement`列表中随机选择一个字符串。
- `colorCheck`：根据传入的字符串决定返回的字符串颜色。如果字符串是"今晚吃夜宵喵~"，则返回绿色的字符串；如果字符串是"今晚不吃夜宵喵~"，则返回红色的字符串。
- `printStatement`：打印出`getRandomStatement`方法获取的随机字符串，并通过`colorCheck`方法设置颜色。

## 如何运行

在命令行中，导航到包含`NightSnake.py`的目录，然后运行以下命令：

```bash
python NightSnake.py