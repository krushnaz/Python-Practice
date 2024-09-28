import re
def validateDate(date) :
    pattern = r"^(\d{2})-(\d{2}|[a-zA-Z]+)-(\d{4})$"
    regex = re.compile(pattern)
    if re.match(regex,date) :
        return True
    else :
        return False
    
date = input("Enter date to validate : ")
if validateDate(date) :
    print("date is valid")
else :
    print("Date is Invalid")
    