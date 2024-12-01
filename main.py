import argparse

def main(book_filename):
    book_path = f"books/{book_filename}"
    text_content = get_text_from_path(book_path)
    word_count = get_word_count(text_content)
    char_count = get_character_count(text_content)
    char_sorted_list = char_dict_to_sorted_list(char_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    
    for char_dict in char_sorted_list:
        if not char_dict["char"].isalpha():
            continue
        print(f"The '{char_dict["char"]}' character was found {char_dict["count"]} times")
    
    print(f"--- End report ---")

def sort_on_count(d):
    return d["count"]

def char_dict_to_sorted_list(char_count):
    char_count_list = []
    for char in char_count:
        char_count_list.append({"char": char, "count": char_count[char]})
    char_count_list.sort(reverse=True, key=sort_on_count)
    return char_count_list

def get_character_count(text):
    char_count = {}
    for char in text:
        c = char.lower()
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count


def get_word_count(text):
    return len(text.split())

def get_text_from_path(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Set your book filename')
    parser.add_argument('book_filename', help='enter the book filename in /books directory')
    args = parser.parse_args()
    main(args.book_filename)
