def filterData(x) :
    if x < 5 :
        return x
    
result = filter(filterData,(1,2,4,6))
print(list(result))