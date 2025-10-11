def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(file_path):
    words = get_book_text(file_path).split()
    num_words = len(words)
    return num_words

def get_num_characters(file_path):
    content = get_book_text(file_path).lower()
    char_count = {}
    for char in content:
        if char not in char_count:
            char_count[char] = 1
            continue
        char_count[char] += 1
    return char_count

def sort_dict_item_to_list(dictionary):
    list = []
    
    for item in dictionary:
        new_dict = {
                "char": item,
                "num": dictionary[item]
            }
        list.append(new_dict)

    def sort_on(items):
        return items["num"]

    list.sort(reverse=True, key=sort_on)

    return list