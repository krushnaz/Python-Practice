# Yield keyword is used to create or generate a generator
# def calSum(n) :
#     myList = []
#     num = 0
#     while num < n :
#         myList.append(num)

#         num = num + 1;
#         print(myList)
#     return myList

# psum = sum(calSum(10))
# print(psum)


# def calSum(n) :
#     num = 0
#     while num < n :
#         yield num;
#         print(num)
#         num = num + 1;

      

# psum = sum(calSum(10))
# print(psum)

# write a proram to calculate the square of given number using generator

# L=[2,4,6,8,10]
# def generator():
#   yield L
# x=generator()
# print(x.__next__())

# def generator() :
#     n = 3;
#     i = 1;
#     while i <= n :
#         yield i
#         i=i+1;
# x = generator()
# for i in x :
#     print(i)



