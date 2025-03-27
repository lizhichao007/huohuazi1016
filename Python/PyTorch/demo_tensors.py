import torch 
import numpy as np

#Tensors can be created directly from data. The data type is automatically inferred.
# print("++++++++++++++++++++(1)++++++++++++++++++++")
# data = [[1,2],[3,4]]
# print(f"data: \n {data}")
# x_data = torch.tensor(data)
# print(f"tensor data: \n {x_data}")
# #From a NumPy array
# print("++++++++++++++++++++(2)++++++++++++++++++++")
# np_array = np.array(data)
# print(f"np_array: \n {np_array}")
# x_np = torch.from_numpy(np_array)
# print(f"x_np: \n {x_np}")
# #From another tensor:
# print("++++++++++++++++++++(3)++++++++++++++++++++")
# x_ones = torch.ones_like(x_data)
# print(f"x_ones: \n {x_ones}")
# x_rand = torch.rand_like(x_data,dtype=torch.float)
# print(f"x_rand: \n {x_rand}")
# #With random or constant values:
# print("++++++++++++++++++++(4)++++++++++++++++++++")
# #shape is a tuple of tensor dimensions
# shape = (2,3)
# print(f"shape: \n {shape}")
# rand_tensor = torch.rand(shape)
# print(f"rand_tensor: \n {rand_tensor}")
# ones_tensor = torch.ones(shape)
# print(f"ones_tensor: \n {ones_tensor}")
# zeros_tensor = torch.zeros(shape)
# print(f"zeros_tensor: \n {zeros_tensor}")
#Attributes of a Tenso
# print("++++++++++++++++++++(5)++++++++++++++++++++")
# tensor = torch.rand(3,3)
# print(f"shape of tensor: {tensor.shape}")
# print(f"datatype of tensor:  {tensor.dtype}")
# print(f"devive tensor is stored on: {tensor.device}")

# We move our tensor to the current accelerator if available
# print("++++++++++++++++++++(6)++++++++++++++++++++")
# if torch.accelerator.is_available():
#     tensor = tensor.to(torch.accelerator.current_accelerator())

# Standard numpy-like indexing and slicing
# print("++++++++++++++++++++(7)++++++++++++++++++++")
# tensor = torch.ones(3,4)
# print(f"tensor:\n {tensor}")
# print(f"first row: {tensor[0]}")
# print(f"first column: {tensor[:,0]}")
# print(f"last column: {tensor[...,-1]}")
# tensor[:1]= 2
# print(tensor)
# tensor[:,1] = 0
# print(tensor)
# You can use torch.cat to concatenate a sequence of tensors along a given dimension. See also torch.stack, another tensor joining operator that is subtly different from torch.cat.
# print("++++++++++++++++++++(8)++++++++++++++++++++")
# t1 = torch.cat([tensor,tensor,tensor],dim=1)
# print(t1)
#Arithmetic operations
# print("++++++++++++++++++++(9)++++++++++++++++++++")
# tensor = torch.rand(3,3)
# print(tensor)
# tensor = tensor.T #转置
# print(tensor)
# print("++++++++++++++++++++(10)++++++++++++++++++++")
# tensor = torch.ones(3,3)
# print(tensor)
# tensor[:,1] = 2
# print(tensor)
# y1, y2, y3 will have the same value
# y1 = tensor @ tensor.T
# print(f"y1 \n {y1}")
# y2 = tensor.matmul(tensor.T)
# print(f"y2 \n {y2}")
# y3 = torch.rand_like(y1)
# print(f"y3 rand like \n {y3}")
# torch.matmul(tensor,tensor.T,out=y3)
# print(f"y3 \n {y3}")

# z1 = tensor * tensor
# print(f"tensor * tensor:\n {z1}")
# z2 = tensor.mul(tensor)
# print(f"tensor mul \n {z2}")
# z3 = torch.rand_like(tensor)
# print(f"tensor rand like:\n {z3}")
# torch.mul(tensor,tensor,out=z3)
# print(f"z3 \n {z3}")

# print("++++++++++++++++++++(12)++++++++++++++++++++")
# agg = tensor.sum()
# agg_item = agg.item()
# print(agg_item,type(agg_item)) #12.0 <class 'float'>

# print("++++++++++++++++++++(13)++++++++++++++++++++")
# tensor.add_(3)
# print(tensor)

# Tensor to NumPy array
# print("++++++++++++++++++++(14)++++++++++++++++++++")
# t = torch.ones(5)
# print(f"t: {t}")
# n = t.numpy()
# print(f"n: {n}")
# t.add_(2)
# print(f"t: {t}")
# print(f"n: {n}")

#NumPy array to Tensor
# print("++++++++++++++++++++(15)++++++++++++++++++++")
# n = np.ones(5)
# t = torch.from_numpy(n)
# print(n)
# print(t)
# np.add(n,2,out=n)
# print(n)
# print(t)
if torch.cuda.is_available():
    print('yes')
else:
    print("no")
