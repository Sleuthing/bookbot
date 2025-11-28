from stats import count_words, count_each_character

def get_book_text(filepath):
    with open(filepath) as file:
        print(f"Analyzing book found at {filepath}...")
        file_content = file.read()
    return file_content

def main():
    print("============ BOOKBOT ============")
    # print(get_book_text("./books/frankenstein.txt"))
    file_content = get_book_text("./books/frankenstein.txt")
    num_words = count_words(file_content)
    print(f"Found {num_words} total words")
    for k,v in count_each_character(file_content).items():
        print(f"{k}: {v}")
    print("============= END ===============")

main()
# if __name__ == 'main':
#     get_book_text("./books/frankenstein.txt")