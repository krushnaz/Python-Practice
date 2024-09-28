import re
def validateURL(url) :
    pattern = r"https?://[^\s/$.?#].[^\s].*"
    regex = re.compile(pattern)
    if regex.match(url) :
        print(f"{url} is Valid ")
    else :
        print(f"{url} is Invalid ")
        
url = "http://www.google.com"
validateURL(url)