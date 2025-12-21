"""
该案例演示整数不同数制的表示形式
二进制：以0b开头
八进制：以0o开头
十进制：正常数字开头
十六进制：以0x开头
"""

#十进制
dec_num = 10
#二进制
bin_num = 0b1010
#八进制
oct_num = 0o12
#十六进制
hex_num = 0xa

print("dec_num =", dec_num)
print("bin_num =", bin_num)
print("oct_num =", oct_num)
print("hex_num =", hex_num)

# 介绍几个函数。 函数：完成某项功能的代码块
print("===============")
print("十进制数字", str(dec_num))
print("转换为二进制数字", bin(dec_num))
print("转换为八进制数字", oct(dec_num))
print("转换为十六进制数字", hex(dec_num))