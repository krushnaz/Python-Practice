import re 
def validateURL(url) :
    pattern = r'^(https|ftp)://[^\s/$.?#].[^\s]*$'
    
    if re.match(pattern,url) :
        return True
    else :
        return False
    
url = "http://www.examle.com"
result = validateURL(url)
if result : 
    print("URL is valid")
else :
    print("URL is Invalid")
    
