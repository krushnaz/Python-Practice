class FindArea :
    def areaOfReact(self,len,wid) :
        self.len = len
        self.wid = wid
        return len * wid;
a1 = FindArea()
area = a1.areaOfReact(10,20)
print("Area of rectangle is :",area)
        