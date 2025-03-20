from stats import book_word_count, character_count, sort_on, create_dict_list, print_dict_list_clean
from string import ascii_lowercase
import sys
def get_book_text(filepath):
    with open(filepath) as file:
        book_text = file.read()
    return book_text


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    word_count = book_word_count(get_book_text(path))
    char_count = character_count(get_book_text(path))
    char_list = create_dict_list(char_count)
    char_list.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    print_dict_list_clean(char_list)
    print("============ END ===========")
    pass

main()
