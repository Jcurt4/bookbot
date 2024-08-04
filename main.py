import string

def main():
    book_location  = "books/frankenstein.txt"
    text = get_book_text(book_location)
    num_words = get_num_words(text)
    char_count = num_characters(text)
    char_list = list_of_dictionaries(char_count)
    fixed_char_list = remove_spec_char(char_list)
    sortable_list = transform_list(fixed_char_list)
    sortable_list.sort(reverse=True, key=sort_on)

    print(f"--- Being report of {book_location} ---")
    print(f"{num_words} words found in the document")
    print_sorted(sortable_list)
    print("--- End report ---")

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

def list_of_dictionaries(char_count):
    list_of_char = []
    for char, count in char_count.items():
        holder_dict = {char: count}
        list_of_char.append(holder_dict)
    return list_of_char

def remove_spec_char(char_list):
    letter_list = []
    for d in char_list:
        filtered_dict = {}
        for key, value in d.items():
            if is_letter(key):
                filtered_dict[key] = value
        letter_list.append(filtered_dict)
    filtered_list = [d for d in letter_list if d]
    return filtered_list

def is_letter(character):
    return character in string.ascii_letters    

def sort_on(sortable_list):
    return sortable_list["num"]

def transform_list(fixed_char_list):
    transfromed_list = []
    for d in fixed_char_list:
        for key, value in d.items():
            new_dict = {"letter": key, "num": value}
            transfromed_list.append(new_dict)
    return transfromed_list

def print_sorted(sortable_list):
    for n in sortable_list:
        print(f"The '{n['letter']}' character was found {n['num']} times")

main()