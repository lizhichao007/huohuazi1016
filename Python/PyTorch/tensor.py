import torch
# Tensor的属性
# a = torch.Tensor(2,3)
# print(a)
# print( a.device) #（cpu/cuda）
# print(a.layout) # 内存布局的对象 对应的是稠密和稀疏，在内存中的存储方式是稠密的，是内存中的连续空间 稀疏存储的是非零元素的坐标
# print(a.dtype)
# 每一个Tensor都有torch.dtype,torch.device,torch.layout
# e.g
# a = torch.tensor([1,2,3],dtype=torch.float,device='cpu')
# print(a)

# 定义稀疏的张量
# torch.sparse_coo_tensor
# coo 类型表示了非零元素的坐标形式
# 稀疏表达的当前数据中非零元素的个数，也就是说当前非零元素的个数越多，说明越稀疏，反之就是稠密
# 秩的概念，线性概念中
# indices = torch.tensor([[1,2,3],[4,5,6]]) #坐标值
# values = torch.tensor([3,4,5],dtype=torch.float32) #数值
# x = torch.sparse_coo_tensor(i,v,[2,4])

dev = torch.device('cpu')
a = torch.tensor([2,3],device=dev,dtype=torch.float32)
print(a)

# 定义一个稀疏的张量
indices = torch.tensor([[0,1,2],[0,1,2]]) #坐标值
values = torch.tensor([3,4,5],dtype=torch.float32) #数值
x = torch.sparse_coo_tensor(indices,values,[4,4])
print(x)
# 将稀疏转化为稠密
x = torch.sparse_coo_tensor(indices,values,[4,4]).to_dense()
print(x)

# 为什么要有这样的操作？
    # 
# 为什么有什么数据存放在CPU，有写数据存放在GPU？
    # 数据读取放在CPU，参数的计算和反向传播GPU，利用率最高，资源的调度和优化
    # 模型调优
