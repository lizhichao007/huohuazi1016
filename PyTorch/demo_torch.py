import torch
# 使用原始数据
a = torch.Tensor([[1,2],[4,5]])
print(a)
print(a.type())
# 自定义形状
a = torch.Tensor(2,3) #随机的值
print(a)
print(a.type()) #torch.FloatTensor
# tensor([[-1.4525e+17,  2.0459e-42,  0.0000e+00],
#         [ 0.0000e+00,  0.0000e+00,  0.0000e+00]])

# 特殊的tensor
a = torch.ones(2,3)
print(a)
print(a.type())

a = torch.eye(3,3)
print(a)
print(a.type())

a = torch.zeros(3,3)
print(a)
print(a.type())

b = torch.Tensor(2,3)
b = torch.zeros_like(b)
print(b)
b = torch.ones_like(b)
print(b)

# 随机
a = torch.rand(2,2) #随机值在0-1之间
print(a)

# 定义正态分布 #标准差
a = torch.normal(mean=0.0,std=torch.rand(5))
print(a)
a = torch.normal(mean=torch.rand(5),std=torch.rand(5))
print(a)

# 均匀分布
a = torch.Tensor(2,2).uniform_(-1,1)
print(a)
print(a.type())

# 序列
a = torch.arange(0,10,1)
print(a) #tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 等间隔获取数  
b = torch.linspace(0,10,2)  #没有获取成功
print(f"b {b}")
# 获取一个打乱顺序的序列
a = torch.randperm(10)
print(a)
