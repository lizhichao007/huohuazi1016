#列表
# list = ['how','are','you','?']
# print(list) #访问整个列表
# print(list[2]) #you
# print(list[0:2]) #['how', 'are']  左闭右开

# #更新列表
# list[2]='u' #['how', 'are', 'u', '?']
# print(list) 
# # 添加
# list.append("please") 
# print(list) #['how', 'are', 'u', '?', 'please']
# # 删除
# del list[0]
# print(list) #['are', 'u', '?', 'please']

# 列表的运算
# question = ['how','are','you','?']
# number = ['1','2','5','4','3']
# answer = ['I','am','fine','!']
# length = len(question)
# print(length) #4
# # 列表相加
# total = question + answer
# print(total) # ['how', 'are', 'you', '?', 'I', 'am', 'fine', '!']
# # 列表复制
# print(question*2) #['how', 'are', 'you', '?', 'how', 'are', 'you', '?']
# print(['hello']*2) #['hello', 'hello']
# #判断元素是否在列表中
# print('how' in question) #True
# #迭代
# for i in question:
#     print(i)

#列表函数的使用
# print(max(answer)) #fine
# print(max(number)) #5

# print(min(answer)) #!
# print(min(number)) #1

# my_list = ['1','3','4','2','3','3','3']
# print(my_list) #['1', '3', '4', '2', '3', '3', '3']
# #增加
# my_list.append(100)
# print(my_list) #['1', '3', '4', '2', '3', '3', '3', 100]
# #翻转
# my_list.reverse()
# print(my_list) #[100, '3', '3', '3', '2', '4', '3', '1']
# #指定位置插入
# my_list.insert(0,'1000000')
# print(my_list) #['1000000', 100, '3', '3', '3', '2', '4', '3', '1']
# my_list[1]='999'
# print(my_list) #['1000000', '999', '3', '3', '3', '2', '4', '3', '1']

# my_list.pop() #删除最后一个元素
# print(my_list) #['1000000', '999', '3', '3', '3', '2', '4', '3']
# my_list.pop(0) #删除指定元素的位置
# print(my_list) #['999', '3', '3', '3', '2', '4', '3']

#列表中的数据元素可以是不同类型的
# shop= [["water",'123'],["junk",'234']]
# print(shop) #[['water', '123'], ['junk', '234']]

# my_list = [1,2,3,4,5,2,3]
# number = my_list.count(2)
# print(number) #2
# print(type(my_list[0])) #<class 'int'>

# print(my_list.index(5)) #4 找出值相匹配的第一个索引
# print(my_list) #[1, 2, 3, 4, 5, 2, 3]
# my_list.remove(3) #移除列表中第一次出现的值
# print(my_list) #[1, 2, 4, 5, 2, 3]

#元组

##注意，列表可以修改，元组是不可以修改的
# my_tuple1 = ('my','name','is',123)
# my_tuple2 = tuple() #创建空元组
# my_tuple3 = (123,)
# print(my_tuple1) #('my', 'name', 'is', 123)
# print(my_tuple2) #()
# print(my_tuple3) #(123,) 如果是一个元素，最后需要添加一个标点符号,
# #索引
# print(my_tuple1.index('is')) #2
# #访问元组
# print(my_tuple1[0]) #my
# print(my_tuple1[1]) #name

# 元组的另一种定义方式
# touple1 ='hi','hello','how','are'
# print(touple1[2]) #how

# 变着花样修改元组
# list1=[12,34]
# tuple2='hi','hello',list1
# print(tuple2) #('hi', 'hello', [12, 34])
# list1[0]='123'
# list1[1]='456'
# print(tuple2) #('hi', 'hello', ['123', '456'])

# 删除整个元组
# print(tuple2)
# del tuple2
# print(tuple2) #NameError: name 'tuple2' is not defined. Did you mean: 'tuple'?

# 元组运算
touple1 ='hi','hello','how','are'
# 求元组的长度
print(len(touple1)) #4
touple2 = ('you',"'I'm fine.")
# 元组连接
print(touple1+touple2) #('hi', 'hello', 'how', 'are', 'you', "'I'm fine.")
# 元组复制
print(touple1*2) #('hi', 'hello', 'how', 'are', 'hi', 'hello', 'how', 'are')
#判断元素是否在元组内
print('hello' in touple1) #True
#迭代
for i in touple1:
    print(i)
# 元组内置函数
print("======")
print(max(touple1))
print(min(touple1))
print(len(touple1))
list3=[1,2,3]
print(list3) #[1, 2, 3]
print(tuple(list3)) #(1, 2, 3)