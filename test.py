import torch

print(torch.cuda.is_available())
from torch.backends import cudnn

print(cudnn.is_available())
x = torch.tensor(1, device = 'cuda')
# print(x)
# dev = torch.device('cuda:0')
# x.to(dev)
print(x)
# print(dev)
print(torch.cuda.device_count())
# print(torch.version.cuda)
print(torch.cuda.get_device_name(0))
