import numpy as np
a=np.random.rand(3)
# 1d array with 3 elements here
print(a)
b=np.random.rand(3,3) # more dim. 3X3 array
print(b)
# 0 to 10 but not 10, only 3 elmenets
c=np.random.randint(0,10,(3,4))
print(c)
arr=np.array([1,2,3],[4,5,6],[7,8,9])
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))