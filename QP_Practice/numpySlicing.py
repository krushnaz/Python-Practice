import numpy as np

arr = np.array([
    [1,2,3,4,5],
    [11,12,13,14,15],
    [21,22,23,24,25],
    [31,32,33,34,35]
])

slice1 = arr[0:2, 1:3]
print("slice 1 : \n",slice1)
slice2 = arr[:,1]
print("slice 2 : \n",slice2)
slice3 = arr[1,:]
print("slice 3 : \n",slice3)

