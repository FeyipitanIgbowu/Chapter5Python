digit_map = {
    "2": "ABC", "3": "DEF", "4": "GHI",
    "5": "JKL", "6": "MNO", "7": "PRS",
    "8": "TUV", "9": "WXY"
}

def phone_words(number):
    if not number:
        return [""]
    first, rest = number[0], number[1:]
    letters = digit_map.get(first, "")
    combos = []
    for letter in letters:
        for tail in phone_words(rest):
            combos.append(letter + tail)
    return combos

print(phone_words("6862377")[:10])
