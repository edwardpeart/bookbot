def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_chars = text.lower()

    char_dict = get_num_chars(lowered_chars)
    sorted_chars = sort_char_counts(char_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_chars(lowered_chars):
    char_dict = {}
    for char in lowered_chars:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict

def sort_char_counts(char_dict):
    sorted_list = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_list


if __name__ == "__main__":
    main()