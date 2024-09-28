def is_palindrome(number) :
    temp = str(number)
    
    if temp == temp[::-1] :

        return True
    return False

result = is_palindrome(121)
if result :
    print("yes")
else :
    print("no")
    