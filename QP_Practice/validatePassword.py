import re
def validatePassword(password) :
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$*])[A-Za-z\d@#$*]{8,20}$"
    
    regex = re.compile(pattern)
    if regex.match(password) :
        return True
    else :
        return False

password = 'Krushna@1'
result = validatePassword(password)
if result :
    print("valid password")
else :
    print("invalid password")
    
    