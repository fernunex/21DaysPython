# https://platzi.com/clases/7967-python-21-dias/63513-encuentra-palabras-con-dos-vocales/

def find_words_with_two_vowels(words):
    return [
        word
        for word in words
        if (word.lower().count('a') + word.lower().count('e') + word.lower().count('i') +
            word.lower().count('o') + word.lower().count('u')) == 2
    ]


words = [
    "hello",
    "Python",
    "world",
    "platzi"
]

words2 = ["text", "test", "python", "example"]

print(find_words_with_two_vowels(words))
print(find_words_with_two_vowels(words2))