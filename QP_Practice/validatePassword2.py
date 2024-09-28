import re 

def validatePassword(password) :
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    regex = re.compile(pattern)
    if regex.match(password) :
        return True
    else :
        return False
    
password = "Krushna"
result = validatePassword(password)
if result :
    print("valid")
else :
    print("Invalid")
    
password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%&*])[a-zA-Z\d!@#$%&*]{8,}$'
email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
