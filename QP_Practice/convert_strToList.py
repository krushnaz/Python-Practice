def create_word_list(string, n):
    word_list = string.split()  # Split the string into words
    return [word for word in word_list if len(word) < n]  # Filter words less than size 'n'

input_string = "Python Programming Language is used for Data Science"
size_limit = 6

words_less_than_n = create_word_list(input_string, size_limit)
print("Words less than size", size_limit, ":", words_less_than_n)
