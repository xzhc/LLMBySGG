"""
    该案例演示了循环的嵌套
    打印9*9乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i} * {j} = {i * j}", end='\t')
    print()
