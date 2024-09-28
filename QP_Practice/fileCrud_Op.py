# Write a program to accept n employee details (eno.ename.salary) from a user and store it in "emp.txt" file. Display the content of remp.txt"    
def storeEmpInfo(filename,data) :
    try : 
        with open(filename,'w') as file :
           for emp in data :
               file.write(f"Emp Id :{emp['eno']},Emp Name : {emp['ename']},Emp Salary : {emp['salary']}\n")     
    except FileNotFoundError as e:
        print(e)
        
def displayEmpInfo(filename) :
    try :
        with open(filename,'r') as file :
            content = file.read()
            print("-----------------reading file data--------------")
            print(content)
    
    except FileNotFoundError as e :
        print(e)
  

try :
    filename = "emp.txt"     
    data = []
    size = int(input("enter size :"))
    
    for i in range(size) :
        eno = int(input(f"enter emp{i+1} Id : "))
        ename = input(f"enter emp{i+1} name : ")
        esalary = float(input(f"enter emp{i+1} salary : "))
        
        data.append({'eno':eno,'ename':ename,'salary':esalary})
    
    storeEmpInfo(filename,data)
    displayEmpInfo(filename)
     
except ValueError as e :
    print(e)
except FileNotFoundError as e :
    print(e)