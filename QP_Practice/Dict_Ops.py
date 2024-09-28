# Write a program to perform the following operations on a dictionary.

# 1. Check whether a given key exists in a dictionary or not.
# 2. Iterate over dictionary items using a for loop.
# 3. Concatenate two dictionaries to create one.
# 4. Sum all the values of a dictionary.
# 5. Get the maximum and minimum value of the dictionary.

def isKeyExists(dict, key) :
    if key in dict :
        print(f"key {key} exists in dictionary")
    else :
        print(f"key {key} does not exists in dictionary")
        
def iterateDict(dict) :
    print("iterating dictionary key and values :")
    for key, values in dict.items() :
        print(f"{key} : {values}")
    
def concatenateDict(dict1, dict2) :
    copyDict1 = dict1.copy()
    copyDict1.update(dict2)
    return copyDict1;

def sumAllDictValues(dict) :
    return sum(dict.values())

def min_max_dict(dict) :
    minimum = min(dict.values())
    maximum = max(dict.values())
    return minimum,maximum

dict1 = {'a' : 10,'b' : 20, 'c': 30, 'd':40, 'e':50}
isKeyExists(dict1, 'b')
iterateDict(dict1)

dict2 = {'f':60, 'g':70}
concatenatedDict = concatenateDict(dict1,dict2)
print(concatenatedDict)

sumOfAllDictVal = sumAllDictValues(dict1)
print("sum of values :",sumOfAllDictVal)

minimum, maximum = min_max_dict(dict1)
print("minimum :",minimum)
print("maximum :",maximum)

