class demo :
    x = 10;
    def display(self,y) :
        self.y = y;
        # print(x)
        # print("hello krushna!")
obj1 = demo()
obj1.display(20)
print(obj1.x,"   ",obj1.y)

obj2 = demo()
obj2.display(30)
print(obj2.x,"   ",obj2.y)
obj2.x = 40
print(obj2.x ,"   ",obj2.y)



