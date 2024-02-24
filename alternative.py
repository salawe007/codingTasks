# creating a fuction to alternate the character
def alternate_characters(string):
    result = ''
    for i in range(len(string)):
        if i % 2 == 0:
            result += string[i].upper()
        else:
            result += string[i].lower()
    return result

# creating a fuction to alternate the words
def alternate_words(string):
    words = string.split()
    result = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            result.append(word.lower())
        else:
            result.append(word.upper())
    return ' '.join(result)

# calling fuctions
def main():
    input_word = input("Enter a string: ")
    
    alternate_chars_result = alternate_characters(input_word)
    print("alternate characters: ", alternate_chars_result)
    
    alternate_words_result = alternate_words(input_word)
    print("alternate words: ", alternate_words_result)

if __name__ == "__main__":
    main()

new = main()

