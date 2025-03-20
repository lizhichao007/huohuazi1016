# 迭代

# python中，可以遍历list或tuple，这种遍历就是迭代

# 实例1
# for i in [1,2,3,4,5]:
#     print(i,end='   ')
# print('\n')

# # 实例2
# for i in 'abcdefg':
#     print(i ,end='  ')
# print()

# # 实例3
#     #迭代字典中的key
# dic = {'name':'libai','age':23,'sex':'boy'}
# for i in dic:
#     print(i,end='   ')
# print('\n')

# # 实例4
#     # 迭代字典中的value
# for i in dic.values():
#     print(i,end='   ')
# print('\n')

# # 实例5
#     # 元组
# tuple1 = (1,2,3)
# print(type(tuple1))
# for i in tuple1:
#     print(i,end='   ')
# print('\n')

# # 实例6
# list1 = [(1,'a'),(2,'b')]
# for x,y in list1:
#     print(x,y,end=' ')
# print('\n')

# python迭代器
    #迭代器是一个可以记住遍历的位置对象
    #迭代器对象从集合的第一个元素开始访问，指导所有的元素被访问结束
    #迭代器只能往前不能后退
    #迭代器有两个方法，iter()和next(),且字符串
    #列表或元组对象都可用于创建迭代器
    #迭代器对象可以使用for进行遍历，也可使用next()函数遍历

# 字符串创建迭代器对象
# str = 'hello'
# iter1 = iter(str)
#     #for循环迭代对象
# for i in iter1:
#     print(i,end='   ')
# print('\n')

# 列表创建迭代器对象
# list2 = [1, 2, 3, 4, 5]
# iter2 = iter(list2)
# while True:
#     try:
#         print(next(iter2),end=' ')  # 使用 iter2 而不是 list2
#     except StopIteration:
#         break
 # 元组创建迭代器
# tuple1 = (1,2,3,4,5)
# iter3 = iter(tuple1)
# while True:
#     try:
#         print(next(iter3),end=' ')
#     except StopIteration:
#         break

# 列表的生成方法
# list1 = list(range(1,10))
# print(type(list1)) #<class 'list'>
# print(list1) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

# # list的创建
# list2 = [i * i for i in range(1,10)]
# print(type(list2)) #<class 'list'>
# print(list2) #[1, 4, 9, 16, 25, 36, 49, 64, 81]

# list3 = [i*i for i in range(1,11) if i % 2 ==0]
# print(list3,end='   ') #[4, 16, 36, 64, 100]

# list4 = [(i,j) for i in range(1,5) for j in range(1,3)]
# print(list4,end='   ') #[(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1), (4, 2)]

# 生成器generator
    # python中，一边循环一边计算的机制，成为生成器：generator
    # 这种操作不必创建创建完整的list，节省大量空间
    # python中，使用yield的函数称为生成器
    # 可以理解为生成器就是一个迭代器

# 生成器的创建
    #注意：列表和生成器的区别就在于括号的差别
# gen = (i*i for i in range(1,10))
# print(gen) #<generator object <genexpr> at 0x0000027AC2D59E00>
# print(type(gen)) #<class 'generator'>
# # for i in gen:
# #     print(i,end='   ')
# # print('\n')
# while True:
#     try:
#         print(next(gen),end='   ')
#     except:
#         break

# 使用函数方式实现生成器
    #定义函数
# def my_function():
#     for i in range(10):
#         print(i)
# my_function()
# print(type(my_function)) #<class 'function'>
    #生成器
# def my_generator():
#     for i in range(10):
#         yield i
# gen = my_generator() 
# print(type(gen)) #<class 'generator'>
# print(next(gen)) #0
# print(next(gen)) #1

# 反向迭代
# for i in range(10):
#     print(i,end='   ')
# for i in reversed(range(10)):
#     print(i,end='   ')

#自己写
# class My_reverse:
#     def __init__(self,start):
#         self.start = start 
#     def __iter__(self):
#         n = self.start
#         while n > 0:
#             yield n
#             n = n-1
#     def __reversed__(self):
#         n=1
#         while n <= self.start:
#             yield n
#             n = n+1
# # for i in reversed(My_reverse(10)):
# #     print(i)
# for i in My_reverse(10):
#     print(i,end='   ')

# 同时迭代多个序列，使用zip()函数
    # 注意，如果两个列表的长度不一种，根据最短的，最短的遍历结束就完成。
ball = ['basketball','volleyball','pingpang ball']
player = ['James','China girls','China man']
# for ball,player in zip(ball , player):
#     print(ball,player)
# 利用zip函数，可以将两个列表组合成一个字典
dict1 = dict(zip(ball,player))
print(dict1)