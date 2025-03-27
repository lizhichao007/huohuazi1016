# 初始化函数
    # 是当创建一个实例的时候，这个函数就会被调用
# class Class_A(object):
#     def __init__(self):  #固定写法
#         print("实例化成功")
# A = Class_A()

# 初始化函数可以传递参数
# class Class_B(object):
#     def __init__(self,name):
#         print('实例化成功')
#         print('name:' + name)
# B = Class_B('huohuazi1016')

# 析构函数
    #类销毁的时候，调用析构函数
# class Class_C(object):
#     def __init__(self):
#         print('实例化成功')
#     def __del__(self):
#         print('实例化销毁')

# C = Class_C()
# del C 

# 继承子类的好处
    # 继承父类的属性和方法
    # 自己定义，覆盖父类的属性和方法

# 调用父类的方法
    # 方法1：
# class Parent:
#     def __init__(self,name):
#         self.name = name
#         print('parent')
#     def say_hello(self):
#         print(f'hello,my name is {self.name}')

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name) #调用父类的方法
#         self.age = age
#         print('child')
#     def  say_hello(self):
#         super().say_hello() #调用父类的say_hello
#         print(f"I am {self.age} years old")

# child = Child('huohuazi',18)
# child.say_hello()
    # 方法2 直接调用父类方法
# class Parent:
#     def say_hello(self):
#         print('parent say hello')
# class Child(Parent):
#     def say_hello(self):
#         Parent.say_hello(self)
#         print('child say hello')

# # 创建实例
# child = Child()
# child.say_hello()
    # 调用父类的构造函数
# class Parent:
#     def __init__(self,name):
#         self.name = name 
#         print('parent')
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#         print('child')
# # 创建实例
# child = Child('huohuazi1016',2)
# print(child.name,child.age)

# 父类方法重写

class Parent:
    par = 2

    def __init__(self,name,age,account):
        self.name = name 
        self.age = age
        self.__account = account

    def get_account(self):
        return self.__account
    
    @classmethod
    def get_name(cls):
        return cls.par
    @property
    def get_age(self):
        return self.age

class Child(Parent):
    def __init__(self, name, age, account, sex):
        super(Child,self).__init__(name, age, account)
        self.sex = sex

if __name__ == '__main__':
    Child = Child('huohuazi1016',2,123456,'boy')
    print(dir(Child))
    print(Child.__dict__)
    print(Child.get_account())
        


