def swapWithoutTem(a,b) :
    # logic 1
    
    # a = a ^ b
    # b = a ^ b
    # a = a ^ b
    
    # logic 2
    a = b - a #10
    b = b - a #10
    a = b + a # 20
    
    # # logic 3
    # a = a + b # 30
    # b = a - b # 10
    # a = a - b # 20
    
    
    return a,b

a,b = swapWithoutTem(10,20)
print(a,b)
    