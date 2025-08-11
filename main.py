from stats import word_counter, get_num_chars, sort_chars
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def prettify_char_count(char_count):
    pretty_list = []
    return_string = ""
    for pair in char_count:
        char = pair["char"]
        num = pair["num"]
        pretty_list.append(f" {char}: {num}")
        
    for combo in pretty_list:
        return_string = return_string + combo + "\n"

    return return_string

def main():
    if sys.argv == [] or sys.argv == ['main.py']:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_book = sys.argv[1]
    book_text = get_book_text(path_book)
    sum_words = word_counter(book_text)
    num_chars = get_num_chars(book_text)
    char_count_sorted = sort_chars(num_chars)

    print(f"============ BOOKBOT ============\n \
Analyzing book found at {path_book}...\n \
----------- Word Count ----------\n \
Found {sum_words} total words\n \
--------- Character Count -------\n \
{prettify_char_count(char_count_sorted)}\n \
============= END ===============")



main()
