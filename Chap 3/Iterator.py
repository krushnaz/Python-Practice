# iterator is a python objects which iterator through list, set, dictionary and tuple 
# iter()
# next()

value = list(n * 2 for n in range(50))
# print(value)
iterObj = iter(value)
while True :
    try:
        items = next(iterObj)
        print(items, end=" ")
    except StopIteration :
        break