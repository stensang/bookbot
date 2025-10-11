import sys
from stats import get_num_words, get_num_characters, sort_dict_item_to_list

def main():
    try:
        text = get_path_to_file()
    except ValueError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(2)

    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_num_characters = sort_dict_item_to_list(num_characters)
    print_report(text, num_words, sorted_num_characters)

def print_report(text, num_words, sorted_num_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_num_characters:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def get_path_to_file():
    script_name, path = sys.argv
    return path

main()