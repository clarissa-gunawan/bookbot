def main():
    book_path = "books/frankenstein.txt"
    text_content = get_text_from_path(book_path)
    word_count = get_word_count(text_content)
    char_count = get_character_count(text_content)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    
    char_list = get_sorted_by_count_filter_by_alpha(char_count)
    for char_dict in char_list:
        print(f"The '{char_dict["character"]}' character was found {char_dict["count"]} times")

def sort_on_count(input):
    return input["count"]

def get_sorted_by_count_filter_by_alpha(char_count):
    char_count_list = []
    for char in char_count:
        if char.isalpha():
            char_count_list.append({"character": char, "count": char_count[char]})
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


main()
