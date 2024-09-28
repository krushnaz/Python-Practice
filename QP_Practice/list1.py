def listOps(string,n) :
    words = string.split()
    filteredWords = [word for word in words if len(word) < n]
    return filteredWords
string = "Python programming language has lot of applications in data analytics"
n = 8
result = listOps(string,n)
print(result)
