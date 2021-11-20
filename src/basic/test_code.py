# *-* coding:utf8 *-*
import os
hello = u"你好，世界"
print(hello)
print(eval("1 + 1"))
print(eval("'*' * 10"))
# __import__('os').popen("dir").read()
print(eval(input("请输入要计算的数字公式：")))
# python内部os.system输出中文乱码
print(os.popen("dir").read())