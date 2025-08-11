def word_counter(string_file):
    word_list = string_file.split()
    return len(word_list)

def get_num_chars(string_file):
    char_dict = {
    }

    string_file_lower = string_file.lower()

    for char in string_file_lower:
        char_dict[char] = 0

    for char in string_file_lower:
        char_dict[char] += 1
    
    return char_dict

def sort_criteria(items):
    return items['num']

def sort_chars(char_dict):
    list_return = []

    for key in char_dict:
        if key.isalpha() == False:
            pass
        else:
            new_dict = {
                "char": key, "num": char_dict[key]
            }   
            list_return.append(new_dict)
            list_return.sort(reverse=True, key=sort_criteria)

    return list_return