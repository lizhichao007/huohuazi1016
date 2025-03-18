# 字典 key-value
# 创建字典
# dic = {"name":'libai',"sex":'boy','age':'21'}
# print(dic) #{'name': 'libai', 'sex': 'boy', 'age': '21'}

# # 访问字典
# print(dic['age']) #21

# # 修改字典
# dic['age']='27'
# print(dic['age']) #27

# # 增加键值对
# dic['level'] = '18'
# print(dic) #{'name': 'libai', 'sex': 'boy', 'age': '27', 'level': '18'}

# # 删除字典
# del dic['sex']
# print(dic) #{'name': 'libai', 'age': '27', 'level': '18'}
# del dic
# print(dic) #NameError: name 'dic' is not defined. Did you mean: 'dir'?

# 使用字典的注意事项
## 字典的键是不允许赋值两次的，如果复制两次就依最后一次赋值的为准
# dic1 = {'name':'libai'}
# dic1['name']='dufu'
# dic1['name'] = 'wangzhihuan'
# print(dic1) #{'name': 'wangzhihuan'}

# 字典的键必须不可变，可是键可以是数字，字符串，元组，但是就是不能用列表
# dic2 = {1:'one','hi':'hello',(1,2,3):'one two three'}
# print(dic2) #{1: 'one', 'hi': 'hello', (1, 2, 3): 'one two three'}
# dic3 = {[1,2,3]:'one two three'}
# print(dic3) #TypeError: unhashable type: 'list'

# 字典的函数方法
# dic = {"name":'libai',"sex":'boy','age':'21',1:1}
#求字典的长度
# print(len(dic)) #4
#输出字典可打印的字符转表示？？？这个没有搞懂是什么意思？？？
# print(str(dic)) #{'name': 'libai', 'sex': 'boy', 'age': '21', 1: 1}
# print(type(dic['name'])) #<class 'str'>
# print(type(dic)) #<class 'dict'>
# print(type(dic[1])) #<class 'int'>

#删除字典内的所有元素
# dic.clear()
# print(dic) #{}

# dic = {"name":'libai',"sex":'boy','age':'21',1:1}
# #浅复制
# dic_copy = dic.copy()
# print(dic_copy) #{'name': 'libai', 'sex': 'boy', 'age': '21', 1: 1}
# # 以列表形式返回字典中所有的值
# print(dic.values()) #dict_values(['libai', 'boy', '21', 1])

# # 随机返回并删除字典中的一对键值
# print("======")
# print(dic.popitem()) #(1, 1)
# print(dic) # {'name': 'libai', 'sex': 'boy', 'age': '21'}
# # 以列表形式返回可遍历的键值元组数组
# print(dic.items()) #dict_items([('name', 'libai'), ('sex', 'boy'), ('age', '21')])
