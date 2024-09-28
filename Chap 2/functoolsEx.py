import functools;
# list1 = [1,2,3,4,5]
# print(functools.reduce(lambda a,b : a + b,list1))

# l = []
# for i in range(1,101) :
#     l.append(i)
# # print(l)
# print(functools.reduce(lambda a,b : a + b,l))
# print(functools.reduce(lambda a,b : a % b,[1,2,3,4,5,6,7,8,9,10]))
# print(functools.reduce(lambda a,b : a + b,['krushna','sangram']))

# print(functools.reduce(lambda a , b :  a if a < b else b, [45, 67 ]))

l = []
count = 0;
for i in range(1,50) :
    if(i % 2 == 0) :
        count+=1;
        l.append(i)
print(l)
print(count)
print(functools.reduce(lambda a,b : a if a > b else b, l))
