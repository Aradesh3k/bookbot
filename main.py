import sys
from stats import num_words
from stats import num_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
        print("Found", num_words(file_contents), "total words")
        print("Here are the found characters:")
        char_count = num_characters(file_contents)
        alpha_char_count = {char: count for char, count in char_count.items() if char.isalpha()}
        sorted_alpha_characters = sorted(alpha_char_count.items(), key=lambda item: item[1], reverse=True)
        for char, count in sorted_alpha_characters:
            print(f"{char}: {count}")

main()