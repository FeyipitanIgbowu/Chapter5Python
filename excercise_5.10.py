def anagrams(words):
    if len(words) <= 1:
        return [words]
    result = []
    for word, character in enumerate(words):
        for char in anagrams(words[:word] + words[word+1:]):
            result.append(character + char)
    return result

print(anagrams("Feyi"))
