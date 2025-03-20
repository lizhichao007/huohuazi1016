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
class Class_E(object):
    name = 'huohuazi1016'
    @classmethod
    def fun_test(self):
        print('name:' + self.name)

A = Class_E()
print(A.name)
A.fun_test()
