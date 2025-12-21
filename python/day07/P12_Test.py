"""
### 文件操作 - 写入和读取文件
1.编写代码创建一个新的文本文件 output.txt，并向其中写入字符串 "This is a test."。
2.读取该文件的内容并打印出来
"""

f = open("output.txt", "w")
f.write("This is a test.\n")
f.close()

f = open("output.txt", "r")
print(f.read())
f.close()