"""
    该案例演示了单分支
    需求：商品价格50，若余额小于50则提示“余额不足，请充值”，最后打印“欢迎下次光临”
"""

from random import randint
balance = randint(1, 100)
print(f"当前余额是：{balance}")
price = 50
if balance < price:
    print("余额不足，请充值")
print("欢迎下次光临")