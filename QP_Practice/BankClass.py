# Create a class "Bank" having attributes "Bank name" "Branch", "City", "Manager Name" and methods" "Change manager name" and "Display details." Wirte a constructor to initialize the instance variables. Write a main program to demonstrate the use of Bank class

class Bank :
    def __init__(self,bankName,branch,city,managerName) :
        self.bankName = bankName
        self.branch = branch
        self.city = city
        self.managerName = managerName
        
    def changeManagerName(self,newName) :
        self.managerName = newName
        print("manager name has change sucessfully!")
        return self.managerName
    
    def display(self) :
        print(f"bank name : {self.bankName}")
        print(f"branch name : {self.branch}")
        print(f"city name : {self.city}")
        print(f"manager name : {self.managerName}")
        
bankDetails = Bank("SBI","Narhe","Pune","Krushna Zarekar")
bankDetails.display()
print("-------------------------------------")
bankDetails.changeManagerName("Sangram Patil")
bankDetails.display()
