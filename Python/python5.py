import logging
#创建一个实例
logger = logging.getLogger(__name__)
# 创建一个处理器
handler = logging.StreamHandler()
# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# 将处理器添加到logger，并设置日志级别
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# 函数
# 计算两个数的和
# def mysum(a,b):
#     return a + b
# print(mysum(2,3)) #5

# # isinstance()进行数据类型检查
# def sum(a,b):
#     if not (isinstance(a,(int,float))) and isinstance(b,(int,float)):
#         raise TypeError("参数类型错误")
#     return a + b
# print(sum(2,2.2)) #4.2
# print(sum('hi',2)) #TypeError: 参数类型错误

# 函数可以返回多个数值
# def mul_value(a,b):
#     value1 = a/b
#     value2 = a%b
#     return value1,value2
# value1,value2 = mul_value(10,5)
# print(value1,value2) #2.0 0
# tuple1=mul_value(20,43)
# print(tuple1) #(0.46511627906976744, 20)  #观察发现返回的数值是以元组的形式返回
# 仔细想想，元组的创建是可以直接用逗号创建的，这里的return返回值就是用逗号来的。符合上了
# 语言中只有python中的函数可以一次返回多个返回值的，而一次接受多个返回值的数据类型就是元组

# 函数的参数

#（1）默认参数
    # 即构造函数时就赋值
    # 注意：只有在形参末尾的那个参数为有效默认参数值，其余不生效
# def params(name, sex = '男'):
#     print('姓名:{}'.format(name),end='')
#     print('性别:{}'.format(sex),end='')

# params('libai')
# logger.info("======")
# params('lishanyin','女')

# 默认参数的值是不可变对象，比如None，True，False，数字或字符串
# def print_info(a,b=[]):
#     print(a)
#     print(b)
#     return b
# result = print_info(1)
# result.append('error')
# logger.info('+++++++++')
# print_info(2)

# 判断默认值是否传入成功
    # 
# __no_value = object() 

# def test (a,b = __no_value):
#     if b is __no_value:
#         raise ValueError("b is not value")
#     return
# print(test(2,3))

# 关键字参数（位置参数）
# def user_info(name,age,sex):
#     print('姓名：{}'.format(name),'年龄：{}'.format(age),'性别：{}'.format(sex),end='')
#     print()
# user_info('libai',23,'boy')
# user_info(name='lishangyin',sex='girl',age='21')

# 不定长参数
# python提供了一种元组方式来接受没有直接定义的参数，需要在参数前边添加星号*
    # 如果在调用的时候没有指定参数，那么就是一个空元组
    # 当然，我们也可以不向函数传递未命名的变量
def user_info (name, age, sex, *hobby):
    print('name:{}'.format(name),end = ' ')
    print('age:{}'.format(age),end = ' ')
    print('sex:{}'.format(sex),end=' ')
    print('hobby:{}'.format(hobby),end=' ')
    return

user_info(name='libai',age='23',sex='boy') #name:libai age:23 sex:boy hobby:() 
user_info('dufu',23,'boy','basketball','pingpang ball','swimming') #name:dufu age:23 sex:boy hobby:('basketball', 'pingpang ball', 'swimming') 

