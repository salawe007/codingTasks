def reverse_last_three_letters(sentence):
    if len(sentence) >= 3:
        reversed_sentence = sentence[:-3] + sentence[-3:][::-1]
        return reversed_sentence
    else:
        return sentence

# Example usage:
input_sentence = "This is a sample sentence"
result = reverse_last_three_letters(input_sentence)
print(result)
