def countLines(content) :
    lines = content.split('\n')
    count = 0
    for i in lines :
        count +=1
    return count

def countVowels(content) :
    vowels = "aeiouAEIOU"
    count = 0
    for i in content :
        if i in vowels :
            count+=1
    return count

try :
    with open("QP_Practice/outputfile.txt",'r') as file:
        content = file.read()
        lineCount = countLines(content)
        vowelCount = countVowels(content)
        
        print(f"Total Lines :{lineCount}")
        print(f"Total Vowels :{vowelCount}")
except FileNotFoundError :
    print("file not found")
    