def main():
    book_location  = "books/frankenstein.txt"
    text = get_book_text(book_location)
    num_words = get_num_words(text)
    character_count = num_characters(text)
    print(character_count)


def get_book_text(book_location):
    with open(book_location) as f:  
        return f.read()
    
def get_num_words(text):
    words_count = text.split()
    return len(words_count)
    
def num_characters(text):
    count = {}
    corrected_text = text.lower().strip()
    for letter in corrected_text:
        if letter in count:
            count[letter] += 1
        elif letter not in count:
            count[letter] = 1
    return count







main()