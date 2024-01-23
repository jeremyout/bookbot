def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    print(get_number_of_words(text))
    print(count_character_dict(text))


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


main()
