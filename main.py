def main():
    book_path = "books/frankenstein.txt"
    text_content = get_text_from_path(book_path)
    num_words = get_num_words(text_content)
    print(num_words)

def get_num_words(text):
    return len(text.split())

def get_text_from_path(path):
    with open(path) as f:
        return f.read()


main()
