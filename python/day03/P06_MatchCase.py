"""
    该案例演示了match ... case
    给定月份，输出对应的月有多少天。
    |是专门用于模式匹配的操作符，它能把多个常量或者模式组合起来，实现 “或” 逻辑。

"""
from random import randint

match month := randint(1, 15):
    case 1|3|5|7|8|10|12:
        print(f"当前月份{month}有31天")
    case 4|6|9|11:
        print(f"当前月份{month}有30天")
    case _:
        print(f"不合理的月份{month}")