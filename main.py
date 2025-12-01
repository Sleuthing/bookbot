from stats import count_words, count_each_character
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        print(f"Analyzing book found at {filepath}...")
        file_content = file.read()
    return file_content

def main(filepath):
    print("============ BOOKBOT ============")
    file_content = get_book_text(filepath)
    num_words = count_words(file_content)
    print(f"Found {num_words} total words")
    for k,v in count_each_character(file_content).items():
        print(f"{k}: {v}")
    print("============= END ===============")

if __name__ == '__main__':
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        print("Missing Filepath.\nUsage: python3 main.py <path_to_book>")
        sys.exit(1)