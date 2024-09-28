class demo :
    def __init__(self) :
        print("constructor called...")
    def __del__(self) :
        print("destructor called....")

d1 = demo() 
d2 = demo() 
del d2
