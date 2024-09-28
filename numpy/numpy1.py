# object is an array interface or method 
# dtype : data type of an array 
# copy : object is copied by default is ture
# order : 

# comparison between List and Array
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import time  # Time complexity
import sys  # Space complexity

# size = 10000
# myList1 = range(size)
# myList2 = range(size)  # Corrected variable name
# myarr1 = np.arange(size)
# print(myarr1)
# myarr2 = np.arange(size)
# start1 = time.time()
# result = [(x, y) for x, y in zip(myList1, myList2)]  # Corrected variable name
# print(time.time() - start1)
# endtime1 = time.time()
# print("execution time for list :",endtime1 - start1)
# start2 =time.time()
# result = myarr1 + myarr2
# endtime2 = time.time()
# print("execution time for array : ",endtime2 - start2) 

# L1 = range(100)
# A1 = np.arange(100)
# print("size of A1 :",A1.size)
# print("item size of A1 :",A1.itemsize)
# print("length of list :",len(L1))
# print("size of element in list :",sys.getsizeof(99))


# a = np.array([1,2,3,4,5])
# print(a)
# print("type :",type(a))
# print("DType :",a.dtype)
# print("Dimentions :",a.ndim)
# print("Shape :",a.shape)
# print("Size :",a.size)
# print("Item size :",a.itemsize)
# print("Sum :",a.sum())
# print("Length :",len(a))
# print("Maximum element :",a.max())
# print("minimum element :",a.min())
# print("Standard diviation  :",a.std())


# L1 = [1,2,3,4,5]
# L2 = [6,7,8,9,10]
# L3 = [11,12,13,14,15]
# L4 = [16,17,18,19,20]

# c = np.array([L1,L2,L3,L4])
# print(c)

# print("Length :",len(c))
# print("Size :",c.size)
# print("Shape :",c.shape)

# a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a1)
# myList = [10,20,30,40,50]
# d = np.array(myList, dtype=float)
# print(d)
# # (2,18),(18,2),(3,12),(12,3),(4,9),(9,4),(6,6)
# x1 = np.arange(36) 
# # print(x1)
# x2 = x1.reshape(9,4)
# # print(x2)

# # x3 = x1.reshape(6,-1)
# # print(x3)

# # x4 = x1.reshape(-1,9)
# # print(x4)

# x5 = x1.reshape(6,6)
# print(x5)
# print("====================")
# print(x5[3:4])
# print("====================")
# print(x5[2:6,1:5])
# A1 = np.linspace(0,10,5)
# print(A1)

# ========================= Operations on array =====================================================
# x = np.array([(1,2,3),(4,5,6),(7,8,9)])
# y = np.array([(10,11,12),(13,14,15),(16,17,18)])

# print(x)
# print(y)
# print("=========Addition=============")
# print(x+y)
# print("=========subtraction=============")
# print(x-y)
# print(np.subtract(y,x))
# print("========= multiplication =============")
# print(x*y)
# print(np.multiply(x,y))
# print("========= Division =============")
# print(x/y)
# print((np.divide(x,y)))
# print("========= Modulo =============")
# print(x%y)
# print((np.mod(x,y)))
# print("========= Power =============")
# print(x**y)
# print((np.power(x,y)))

print("========= Arrange and reshape together =============")
b2 = np.arange(0,49,2)
# print(b2)
# print(b2.size)
b2 = np.arange(0,49,2).reshape(5,5)
# print(b2)

col = np.array([1,2,3,4,5]).reshape(1,5)
newarr = np.append(b2,col,axis=0)
# print(newarr)
# print(type(newarr))

b3 = np.insert(b2,1,[10,20,30,40,50],axis=1)
# print(b3)

b3 = np.insert(newarr,1,[20,30,40,50,60,70],axis=1)
# print(b3)

np.delete(b3,5,axis=1)
print(b3)






#======================================== NumPy ==============================================================
# arr = np.zeros([2,4],dtype= float)
# print(arr)
# print(type(arr))

# arr = np.ones([2,3],dtype=int)
# print(arr)

# arr = np.empty([1],dtype=int)
# print(arr)

# arr = np.arange(5,30,5)
# print(arr)

# print(np.arange(1.5))

# arr = np.array([10,20,30])
# add = arr + 5
# print(add)
# print(type(add))


#-================================ Scalar ======================================================

# arr = np.array([10,20,30])
# sub = arr - 5
# print(sub)
# print(type(sub))

# arr = np.array([10,20,30])
# mul = arr * 2
# print(mul)
# print(type(mul))

# arr = np.array([10,20,30],dtype=int)
# div = (arr / 2)
# print(div)
# print(type(div))

# ========================================================================================================

# arr = np.array(((1,2,3),(4,5,6)))
# print(arr)

# print("shape of array :",arr.shape)
# print("number of diamention : ",arr.ndim)
# print("size of array :",arr.size)
# print("type of element in array :",arr.dtype)
# print("number of bytes in array :",arr.nbytes)

# ==========================Arthematic Operation ====================================================

# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# print("addition is :",np.add(a1,a2))
# print("Substrsction is :",np.subtract(a2,a1))
# print("MUltiplication is :",np.multiply(a2,a1))
# print("dividation is :",np.divide(a2,a1))
# print("Power is :",np.power(a2,a1))
# print("modulo is :",np.mod(a1,a2))

# ====================
# Array Multiplication
# ====================
# a1 = np.array([1,2,3])
# a2 = np.array([4,5,6])
# print(np.dot(a1,a2))
# print(np.cross(a1,a2))

# ==================== Array Transposition =================================================
# arr =  np.array(([1,2,3],[4,5,6]))
# print(arr)
# print(np.transpose(arr))


# ======================= Universial Array Function =============================================

# ======================
# Trignometric functions 
# ======================

# angles = np.array([0,30,45,60,90,180])
# radian = np.deg2rad(angles)
# # print(radian)

# print("sin of angle in array :")
# sin_value = np.sin(radian)
# print(sin_value)

# print("cosine of angle in array :")
# cos_value = np.cos(radian)
# print(cos_value)

# print("tangent of angle in the array :")
# tan_value = np.cos(radian)
# print(tan_value)

# ====================
# Statistical Function
# ====================

# number = np.array([10,20,30,40,50])

# print("Minimum and  Maximum number :")
# print(np.min(number),np.max(number))

# print("number is which is below 70% :")
# print(np.percentile(number,70))

# print("Mean value of the number :")
# print(np.mean(number))

# print("standard diviation of number :")
# print(np.std(number))

# print("Avarage value of the number :")
# print(np.average(number))

# print("Variance of the number :")
# print(np.var(number))


# ================
# Bit-twidunctions
# ================

# a = 10
# b = 12

# print("binary representation of :a",bin(a))
# print("binary representation of :a",bin(b))

# print("bitwise_and  of a and b :",np.bitwise_and(a,b))
# print("bitwise_or of a and b :",np.bitwise_or(a,b))

# c = 22
# print("Invsrsion of number :",np.invert(c))

# print("left_shift of 10 by 2 bits :",np.left_shift(10,2))
# print("right_shift of 10 by 2 bits :",np.right_shift(10,2))





















