import re
# var = 'huohuazi1016|libai'
# result = re.findall('libai',var)
# print(result)
# if len(result) > 0:
#     print('yes')
# else:
#     print('no')

# var1 = 'huohuazi|李白'
# result = re.findall('[a-z]',var1)
# print(result)

# 闭包
    # 这种内部函数的局部作用域中可以访问外部函数局部作用域中变量
    # 的行为，我们称之为闭包。
    # 换言之，当某个函数被当成对象返回时，夹带了外部变量，就形成了闭包
# time = 0
# def study_time(time):
#     def insert_time(min):
#         # nolocal表示函数或其他作用域中使用外层（非全局）变量
#         nonlocal time
#         time = time + min
#         return time
#     return insert_time

# f = study_time(time)
# print(f(2))
# print(time)
# print(f(100))
# print(time)
# # 验证闭包
# print(f.__closure__) #(<cell at 0x0000023164ABD720: int object at 0x0000023164980D90>,)
# print(f.__closure__[0].cell_contents)

import time

# 装饰器
    # 1 接受一个函数
    # 2 嵌套一个包装函数，包装函数会接受原函数相同参数，并执行原函数，还会执行附加功能
    # 3 返回嵌套函数
# 方式1
# def print_info():
#     print('name: huohuazi1016')

# def decorator(func):
#     def print_info():
#         print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
#         func()
#     return print_info

# f = decorator(print_info)
# f()
# 方法2

# def decotator(func):
#     def infomation():
#         print(time.strftime('%Y-%m-%d',time.localtime(time.time())))
#         func()
#     return  infomation

# @decotator
# def information():
#     print('name:huohuazi1016')

# information()
# 以上的信息不能变动，要是想修改人名等其他信息就比较麻烦
# 使用以下方法
# def decorator(func):
#     def print_info(*args,**kwargs):
#         print(time.strftime('%Y-%m-%d'),time.localtime(time.time()))
#         func(*args,**kwargs)

# @decorator
# def print_info(name,age):
#     print('name:' + name + ' ' + 'age:' + age)

# print('huohuazi1016',2)

