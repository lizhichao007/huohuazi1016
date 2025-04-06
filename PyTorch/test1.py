import torch
import numpy as np

# data = [[1,2],[3,4]]
# print(f"data: \n {data}")
# # print("=================(1)=================")
# x_data = torch.tensor(data)
# print(f"x_data: \n {x_data} \n")
# np_array = np.array(data)
# print(f"np_data: \n {np_array}")
# x_np = torch.from_numpy(np_array)
# print(f"x_np: \n {x_np}")
# x_ones = torch.ones_like(x_data)
# print(f'ones tensor: \n {x_ones} \n')

# x_rand = torch.rand_like(x_data,dtype=torch.float)
# print(f"random tensor: \n {x_rand} \n")

# print("=================(2)=================")
# shape = (2,3)
# rand_tensor = torch.rand(shape)
# ones_tensor = torch.ones(shape)
# zeros_tensor = torch.zeros(shape)

# print(f"random tensor: \n {rand_tensor} \n")
# print(f"ones tensor: \n {ones_tensor} \n")
# print(f"zeros tensor: \n {zeros_tensor} \n")

# print("=================(3)=================")
tensor = torch.ones(3,3)
tensor[:,1] = 2
# print(tensor)

# print("=================(4)=================")
# t1 = torch.cat([tensor,tensor,tensor],dim=1)
# print(t1)

# print("=================(5)=================")
# This computes the element-wise product
# print(f"tensor.mul(tensor) \n {tensor.mul(tensor)} \n")
# # Alternative syntax:
# print(f"tensor*tensor \n {tensor*tensor}")
# print("=================(6)=================")
# This computes the matrix multiplication between two tensors
# print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
# # Alternative syntax:
# print(f"tensor @ tensor.T \n {tensor @ tensor.T}")
# print("=================(7)=================")
# print(tensor,"\n")
# tensor.add_(5)
# print(tensor)
# print("=================(8)=================")
# Tensor to NumPy array
# t= torch.ones(5)
# print(f"t: {t}")
# n = t.numpy()
# print(f"n: {n}")
# print("=================(9)=================")
# # A change in the tensor reflects in the NumPy array.
# t.add_(2)
# print(f"t: {t}")
# print(f"n: {n}")
# print("=================(10)=================")
n = np.ones(5)
t = torch.from_numpy(n)
print(n)
print(t)
np.add(n,1.2,out=n)
print(f"t: {t}")
print(f"n: {n}")

# print("=================(11)=================")
# tensor = torch.rand(3,4)
# print(tensor)
# print(f"shape of tensor: {tensor.shape}")
# print(f"datatype of tensor: {tensor.dtype}")
# print(f"device tensor is stored on: {tensor.device}")

# print("=================(12)=================")
# if torch.cuda.is_available():
#     tensor = tensor.to('cuda')
#     print(f"device tensor is stored on: {tensor.device}")
# else:
#     print(f"cuda is not available.")