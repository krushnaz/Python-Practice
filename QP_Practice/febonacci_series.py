def febo_generator() :
    a,b = 0,1
    while True :
        yield a
        a,b = b, a + b
        
num_terms = int(input("enter terms"))
for term in febo_generator() :
    if term >= num_terms :
        break
    print(term)