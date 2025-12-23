import sys
from stats import get_book_data


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        num, dic = get_book_data(sys.argv[1])
        print(f"============ BOOKBOT ============\n Analyzing book found at books/frankenstein.txt...\n ----------- Word Count ----------\n Found {num} total words\n --------- Character Count -------")
        for items in dic:
            if items["char"].isalpha():
                print(f"{items['char']}: {items['num']}")
        print("============= END ===============")


main()
