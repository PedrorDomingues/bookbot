import sys
from stats import (
    get_num_words, 
    char_count, 
    dic_sort,
    get_book_text
)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    book = get_book_text(book_path)
    num_words = get_num_words(book)
    dic = char_count(book)
    dic = dic_sort(dic)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for key in dic:
        if key.isalpha():
            print(f"{key}: {dic[key]}")

    print("============= END ===============")
        
    

main()