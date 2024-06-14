def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_chars = text.lower()
    num_chars = get_num_chars(lowered_chars)
    print(f"{num_words} words found in the document")
    print(f"Number of each letter in the document {num_chars}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def get_num_chars(lowered_chars):
    char_dict = {}
    for char in set(lowered_chars):
        if char.isalpha():
            char_dict[char] = lowered_chars.count(char)
    return char_dict

if __name__ == "__main__":
    main()

   
