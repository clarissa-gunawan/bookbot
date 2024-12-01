def main():
    book_path = "books/frankenstein.txt"
    text_content = get_text_from_path(book_path)
    word_count = get_word_count(text_content)
    char_count = get_character_count(text_content)
    print(f"Book: {book_path}")
    print(f"Word Count: {word_count}")
    print(f"Char Count: {char_count}")

def get_character_count(text):
    char_count = {}
    text = text.lower()
    for char in text:
        try:
            char_count[char] += 1
        except KeyError as e:
            char_count[char] = 1
        except Exception as e:
            print(f"Error: {e}")
    return char_count


def get_word_count(text):
    return len(text.split())

def get_text_from_path(path):
    with open(path) as f:
        return f.read()


main()
