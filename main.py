def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    char_dict = count_character_dict(text)
    generate_report(book_path, number_of_words, char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_number_of_words(text):
    words = text.split()
    return len(words)

def count_character_dict(text):
    letter_dict = {}
    for char in text.lower():
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def generate_report(path, word_count, character_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    list_of_chars = list(character_dict.items())
    list_of_chars.sort(key=lambda x: x[1], reverse=True)
    
    for char in list_of_chars:
        if char[0].isalpha():
            print(f"The {char[0]} character was found {char[1]} times")

    print("--- End report ---")


main()
