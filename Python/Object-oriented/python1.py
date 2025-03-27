# 定义和调用
# class Test():
#     var1 = 0.1
#     var2 = 'libai'
#     var3 = 10
#     def print_info():
#         print('hello')

# print(Test) #<class '__main__.Test'>
# print(Test.var1)
# print(Test.var2)
# print(Test.var3)
# print(Test.print_info) #<function Test.print_info at 0x0000027BF59564D0>
# Test.print_info() #hello

# 类方法调用类属性
    # 用@classmethod声明该方法是类方法，只有声明，才能使用。
    # 使用方法：属性.变量名
# class Test_A():
#     name = 'huohuazi1016'
#     @classmethod
#     def print_name(_name):
#         print('姓名：'+_name.name)
# print(Test_A.name) #huohuazi1016
# Test_A.print_name()

# 类方法传参
# class Test_B():
#     name = 'huohuazi1016'
#     @classmethod
#     def fun(_name,age):
#         print('我是：'+ _name.name)
#         print("年龄：" + str(age))
# Test_B.fun(18)

# 内部修改和增加类属性
# class Test_C():
#     name = 'huohuazi1016'
#     @classmethod
#     def fun(params):
#         print('name:'+params.name)
#         #修改
#         params.name = input("please input your name:")
#         print('name:'+ params.name)
#         #新增
#         params.new_name = input('please input new name:')
#         print('new name:'+ params.new_name)

# Test_C.fun()

# 外部增加和修改类属性
# class Test_D():
#     name = 'huohuazi1016'
#     @classmethod
#     def fun(params):
#         print("name:"+ params.name)
# Test_D.fun()
# Test_D.name = input('please input new name:')
# Test_D.fun()
# Test_D.new_name = input('please input new name:')
# print(Test_D.new_name)

# 类的实例化
# class Class_E(object):
#     name = 'huohuazi1016'
#     def fun_test(self):
#         print('name:' + self.name)

# A = Class_E()
# print(A.name)
# A.fun_test()

# 一个类可以创造多个实例
# class Class_F(object):
#     name = 'huohuazi1016'
#     def my_fun_info(self):
#         print("name: " + self.name)
# # 测试1
# a = Class_F()
# a.my_fun_info()
# print(a.name)
# # 测试2
# b = Class_F()
# print(b.name)
# b.my_fun_info()

# 类属性变化，实例属性会发生变化吗？
# class Class_G(object):
#     name = 'huohuazi1016'
#     def print_name(self):
#         print('name: ' + self.name)

# A = Class_G()
# # A.print_name()
# # Class_G.name='libai'
# # A.print_name()
#     # 通过测试，发现类属性改变，实例属性会跟着变化

# # 实例属性改变了，类属性会改变吗？
# A.name = 'libai'
# print(Class_G.name)
#     # 发现，实例属性改变，不会影响类属性
#     # 不管实例对象怎么修改属性值，对类的属性还是没有影响的。


# 实例方法和类方法

    # 结论：类方法改变，实例方法也会跟着改变
class Class_H(object):
    name = 'huohuazi1016'
    def my_info(self):
        print('name:' + self.name)

A = Class_H()
A.my_info()

def my_new_info():
    print('火华子1016')

A.my_info=my_new_info
A.my_info()
