# fruits = ['apple','banana','cherry']
# print(list(map(str.upper,fruits)))

# fruits = ['apple','banana','cherry']
# print(list(map(len,fruits)))

celsius_temp = [0,40,30,20,60]
result = list(map(lambda c : (c *9/5)+32,celsius_temp))
print(result)
