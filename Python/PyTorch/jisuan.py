import  torch
##add
# a = torch.ones(2,2)
# data = [[2,2],[2,2]]
# b= torch.Tensor(data)
# c = torch.eye(2,2)


# print(a+b)
# print(a.add(b))
# print(torch.add(a,b))
# print(a.add_(b))  #注意，此处的加法运算修改了a中的数值
# print(a)

# sub
# print(a - b)
# print(a.sub(b))
# print(torch.sub(a,b))
# print(a.sub_(b))
# print(a)

# mul 
# print(a*b)
# print(a.mul(b))
# print(torch.mul(a,b))
# print(a.mul_(b))
# print(a)

# div
# print(a/b)
# print(a.div(b))
# print(torch.div(a,b))
# print(a.div_(b))
# print(a)

# 矩阵运算
# data = [[1,2],[3,4]]
# a= torch.Tensor(data)
# b = torch.eye(2,2)
# print(a)
# print(b)
# print("==========")
# print(a@b)
# print(a.matmul(b))
# print(torch.matmul(a,b))
# print(torch.mm(a,b))
# print(a.mm(b))

# 高维tensor
# a = torch.ones(1,2,3,4)
# print(a)
# b= torch.ones(1,2,4,3)
# print(b)
# print(a.matmul(b))
# print(a.matmul(b).shape)

# pow
# a= torch.tensor([2,3])
# print(a)
# print(torch.pow(a,3))
# print(a.pow(3))
# print(a**3)
# print("===")
# print(a.pow_(3))
# print(a)

#exp

# a = torch.tensor([1,2],dtype=torch.float32)
# print(a.type())
# print(a.exp())
# print(a.exp_())
# print(torch.exp(a))
# print(torch.exp_(a))

# log

# a = torch.tensor([1,2],dtype=torch.float32)
# print(torch.log(a))
# print(torch.log_(a))
# print(a.log())
# print(a.log_())

# sqrt

a = torch.tensor([[2,4],[3,9]],dtype=torch.float32)
print(a)
print(torch.sqrt(a))
print(torch.sqrt_(a))
print(a.sqrt())
print(a.sqrt_())

