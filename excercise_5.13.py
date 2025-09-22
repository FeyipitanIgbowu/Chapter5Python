letter_to_digit = {}
for first, second in digit_map.items():
    for character in second:
        letter_to_digit[character] = first

def word_to_number(word):
    result = ""
    for character in word.upper():
        result += letter_to_digit.get(character, "?")
    return result

print(word_to_number("BIGDATA"))
