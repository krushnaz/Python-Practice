def is_leap_year(year) :
    if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
        return True
    return False

result = is_leap_year(2012)
if result :
    print("yes")
else :
    print("No")