from stats import count_words, count_each_character

def get_book_text(filepath):
    with open(filepath) as file:
        file_content = file.read()
    return file_content

def main():
    # print(get_book_text("./books/frankenstein.txt"))
    file_content = get_book_text("./books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"Found {num_words} total words")
    print(count_each_character(file_content))

main()
# if __name__ == 'main':
#     get_book_text("./books/frankenstein.txt")