x = {3,1,2,4,5,6,1,2,3}
# print(type(x))
print(x)
# for i in x :
#     print(i, end=" ")
# print()
# print("lenth :",len(x)) # it gives the total number of elements
# print("sum : ",sum(x)) # it count total of element of set and returns the sum
# print(max(x)) # it returns maximum element of set
# slicing and indexing is not allowed in set
# x1 = set({3,2,4,5,7})
# print(x1)
# x2 = set({'A','B'})
# print(x2)
# x2.add('c')
# print(x2)
# temp = ('q','e','r')
# x2.add(temp)
# print(x2)
# x.update([10])
# print(x)
# print(x.remove(10))
# print(x)
# x.discard(10)
# print(x)
# x.clear()
# print(x)
# print(x.pop())
# print(x.pop())
# print(x.pop())
x4 = x.copy()
# print(x)
# print(x4)
x2 = {3,1,2}
# print(x.union(x4))
print(x.issubset(x2))
print(x.intersection(x2))
print(x.difference(x2))
print(x2.difference(x))