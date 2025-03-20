# 循环
# break continue pass
# for 循环
# for i in range(5):
#     if i == 2:
#         break #终止循环，跳出整个循环
#     print(i)
# print("======（1）========")
# for i in range(5):
#     if i ==2:
#         continue #跳出本次循环，执行下一次循环
#     else:
#         print(i)
# print("======（2）========")
# for i in range(5):
#     if i ==2:
#         pass #空语句，保持结构完整性
#     else:
#         print(i)
# # 输出结果
# # 0
# # 1
# # ======（1）========
# # 0
# # 1
# # 3
# # 4
# # ======（2）========
# # 0
# # 1
# # 3
# # 4

# # range函数使用
# # 上边已经演示了range的一种用法，下边介绍另一种用法
# print("======（3）========")
# for i in range(0,10,2):
#     print(i)

# while循环语句
i=sum=0
while i <=100:
    sum = sum + i
    i = i + 1
print(sum)

# for 和 while 的区别
#（1）for循环只要用于迭代
#（2）while循环主要在满足一定条件为真，反复执行的情况。

# 嵌套循环
# 9*9口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}X{}={}\t'.format(i,j,i*j),end='')
    print()
# 判断闰年
year = int(input("输入一个年份："))
if (year % 4) ==0 and (year % 100) != 0 or (year % 400) ==0:
    print('{}是闰年'.format(year),end='')
else:
    print('{}不是闰年'.format(year),end='')

# if条件判断和嵌套 
    # 这里省略
