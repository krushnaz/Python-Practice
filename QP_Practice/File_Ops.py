def countWords(content) :
    words = content.split()
    return len(words)

def countChar(content) :
    return len(content)

def countVowels(content) :
    vowels = 'aeiouAEIOU'
    count = 0
    for char in content :
        if char in vowels :
           count += 1
    return count

def countLines(content) :
    count = content.split('\n')
    return len(count)

def reverseWords(content) :
    words = content.split()
    reversed_words = [word[:: -1] for word in words]
    return ' '.join(reversed_words)

def main() :
    try :
        with open('/home/krish/Documents/Programming Languages/Python/outputfile.txt','r') as file :
            content = file.read()
            
            print("number of words :",countWords(content))
            print("number of characters :",countChar(content))
            print("number of lines :",countLines(content))
            print("number of vowels :",countVowels(content))
            print("reverse words :",reverseWords(content))
    except FileNotFoundError as e :
        print(e)
    

main()