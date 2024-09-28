def remove_vowels(inputStr) :
    result = " "
    vowels = "aeiouAEIOU"
    for char in inputStr :
        if char not in vowels :
            result += char
    return result
       
userString = input("enter a string")
result = remove_vowels(userString)
print(result)
