# 模块中不仅可以存放变量，还能存放函数，还能存放类
# 一个py文件就可以成为一个模块
# 模块可以自己编写，也可以应用第三方模块
# import math 
# print(math.pi)
# import sys
# print(sys.path)
# #print(version) # 会报错

# from sys import version
# print(version)  #这样就不会报错

# from sys import *
# print(version)
# print(executable) #执行路径

# 主模块和非主模块的定义

# 在python中，如果一个函数调用了其他函数完成了一项功能，我们称这个函数为主函数，如果一个函数没有调用
# 其他函数，我们称这种函数为非主函数。
