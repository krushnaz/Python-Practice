import pandas as pd
import numpy as np

# data = {
#     'ID':[1001,1002,1003],
#     'Name':['Mohan','Sachin','Virat'],
#     'HRA' :[12000,13000,11000],
#     'TA' :[6000,5000,4000],
#     'DA':[1000,9000,8000]
# }
# df = pd.DataFrame(data)
# sumOfEachColumn = df.sum()
# print("sum of each column :\n",sumOfEachColumn)
# meanOfIntegerCol = df[['ID','HRA','TA','DA']].mean()
# print("mean of integer column")
# print(meanOfIntegerCol)

# medianOfIntegerCol = df[['ID','HRA','TA','DA']].median()
# print("median of integer column")
# print(medianOfIntegerCol)

# 3X3 matrix

# array = np.array([
#     [1,2,3],
#     [5,6,7],
#     [9,10,11]
# ])

# # display column wise mean and median
# col_mean = np.mean(array,axis=0)
# col_median = np.median(array,axis=0)

# print("column wise mean :")
# print(col_mean)

# print("column wise median :")
# print(col_median)


# series from numpy array 
array = np.array([1,2,3,9,8,4,5,6,7])
series = pd.Series(array)
min = np.min(series)
max = np.max(series)

print(min)
print(max)