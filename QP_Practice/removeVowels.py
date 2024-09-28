def removeVowels(string) :
    vowels = "aeiouAEIOU"
    new_str = ''
    for i in string :
        if not i in vowels :
            new_str += i
          
    return new_str
  
result = removeVowels("krushna")
print(result)

password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%&*?])[A-Za-z0-9\d!@#$%&*?]{8,20}$'
email = r'^[A-Za-z0-9._%-+]+@[A-Za-z0-9.-]\.[A-Za-z]{2,}$'
url = r'^(https|ftp)://[^\s/$.?#][^\s]*$'
date = r'^(\d{2})-(\d{2}|[A-Za-z]+)-(\d{4})'