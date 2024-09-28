def occurrence(string, sub_string):
    occurrence_list = []
    start_index = 0
    while True:
        index = string.find(sub_string, start_index)
        if index == -1:
            break
        occurrence_list.append(index)
        start_index = index + 1
    return occurrence_list

string = "krushna Sopan Zarekar"
sub_string = "krushna"
occurrences = occurrence(string, sub_string)
print(occurrences)
