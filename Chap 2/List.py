# print(list([1]))
# print(list(["krushna"]))
# print(list("krushna"))
# myList = list([10,20]);
# list2 = [1,2]
# print(myList)
# myList.append(60)
# print(myList[1])
# myList.append(list2)
# print(myList)
# print(myList[2][0])

# for i in range(0,50,2) :
#     myList.append(i)
# print(myList,end=" ")
# print(myList)

# del myList[1]
# print(myList)
# myList.remove(10)
# print(myList)

# print()


# Add element in the list betweeen 1 to 100
# list1 = [];
# listEven = []
# listOdd = []
# for i in range(101) :
#     list1.append(i)
#     if(i % 2 == 0):
#         listEven.append(i)
#     else :
#         listOdd.append(i)


# print("total elements :")
# print(list1)
# print("Odd :")
# print(listOdd)
# print("Even :")
# print(listEven)

# product = ['pencil','pen','eraser','scale','box']
# price = [5,10,2,12,30]
# brand = ['camlin','rotomac','natraj','camel','apsara']
# stationary = [product,price,brand]
# print(stationary)

# stationary[0][0] = "Notebook"
# print(stationary)
# stationary[1][0] = 30
# print(stationary)
# stationary[2].insert(0,"Navneet")
# print(stationary)
# stationary[0].insert(1,"Pencil")
# print(stationary)
# list1 = stationary.copy()
# stationary.clear()
# print(stationary)
# print(list1)

# list1 = [1,2,3,4]
# list2 = [5,4,3,2,1]

# # list1.extend(list2)
# list1.append(list2)

# # print(list1)
# # print(list1.count(4))
# # print(list1.pop(4))
# # print(list1)

# # print(list1.index(4))
# # print(list1.pop(3))
# list1.sort(reverse=True)
# list1.reverse();

# print(list1)


# list1 = [9,8,7,6,5,4,3,2,1,8,7,6,5,4,3]
# # list2 = [5, 4, 3, 2, 1]

# # list1.extend(list2)
# # list1.sort()
# list1.sort(reverse=True)
# # list1.reverse()

# print(list1)

# list1 = []
# for i in range(51) :
#     # if(i == 0) :
#     #     continue
#     if(i % 2 == 0) :
#         list1.append("{} is Even".format(i))
#     else :
#         list1.append("{} is Odd".format(i))
# print(list1)

# list1 = [
#     "{} is Even".format(i) if i % 2 == 0 else "{} is Odd".format(i)
#     for i in range(51)
# ]
# print(list1)

# list1 = [9,8,7,6,5,4,3,2,1,8,7,6,5,4,3]

# l1 = []
# l2 = []
# i = 0
# while(i < (len(list1))) :
#     if(i < (len(list1)) / 2) :
#         l1.append(i)
#         l1.sort()
#     else :
#         l2.append(list1[i])
#         l2.sort(reverse=True)
#     i += 1;
# print(l1)
# print(l2)
# print(l1 + l2)

l1 = [ "{} is Even ".format(i) if i % 2 == 0 else "{} is Odd".format(i) for i in range(51)] 
print(l1)



