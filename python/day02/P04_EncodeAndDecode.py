"""
该案例演示了字符编码以及解码
编码：字符 --->字节
解码：字节 --->字符
"""

str1 = '你好帅'
print(str1)
print(type(str1))
#编码
byte1 = str1.encode('utf-8')
print(byte1)
print(type(byte1))
#解码
str2 = byte1.decode('utf-8')
print(str2)
print(type(str2))

# 注意：编码和解码需要指定相同的字符集
str3 = byte1.decode('gbk')
print(str3)