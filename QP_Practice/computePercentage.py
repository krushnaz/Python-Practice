class studInfo :
    def __init__(self) :
        self.studName = None
        self.studRollNo = None
        self.studMarks = {}
    
    def getData(self) :
        self.studName = input("Enter Student Name :")
        self.studRollNo = int(input("Enter Student Roll No :"))
        for i in range(5) :
            subject = input(f"enter subject{i+1}")
            marks = float(input("enter marks :"))
            self.studMarks[subject] = marks
        
    
    def display(self) :
        totalMarks = sum(self.studMarks.values())
        percentage = totalMarks/5
        
        print(f"student Name :{self.studName}")
        print(f"Student Roll No : {self.studRollNo}")
        print("Student Result :")
        for subject, mark in self.studMarks.items() :
            print(f"{subject} : {mark}")
            
        print(f"Student Percentage {percentage}")
    
    
obj = studInfo()
obj.getData()
obj.display()