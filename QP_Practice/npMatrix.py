import numpy as np

matrix = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

col_mean = np.mean(matrix,axis=0)
col_median = np.median(matrix,axis=0)

row_mean = np.mean(matrix, axis=1)
row_median = np.median(matrix, axis=1)

print(f"column mean : {col_mean}")
print(f"column median : {col_median}")

print(f"row mean :{row_mean}")
print(f"row median :{row_median}")
