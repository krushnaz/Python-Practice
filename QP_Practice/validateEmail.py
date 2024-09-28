import re
def validateEmail(email) :
    pattern = r"^[a-zA-z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-z]{2,}$"
    
  
    if re.match(pattern,email) :
        return True
    else :
        return False
    
email = input("Enter Email Address")

if validateEmail(email) :
    print("valid Email Address")
else :
    print("Invalid Email Address")
    
    