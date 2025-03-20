from string import ascii_lowercase
def book_word_count(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    char_counts = {}
    book_text = book_text.lower()
    for c in ascii_lowercase:
        num = 0
        for char in book_text:
            if char == c:
                num += 1
        char_counts[c]  = num

    return char_counts

def sort_on(dict):
    return dict["num"]

def create_dict_list(dict):
    new_list = []
    for key in dict:
        new_list.append({"char": key, "num": dict[key]})
    return new_list

def print_dict_list_clean(my_list):
    for item in my_list:
        print(f"{item['char']}: {item['num']}")