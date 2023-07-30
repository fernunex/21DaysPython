# https://platzi.com/clases/7967-python-21-dias/63515-calcula-la-longitud-de-las-palabras/

def count_words_by_length(words):
    lenght_words = [len(word) for word in words]

    return {
        len(word): lenght_words.count(len(word))
        for word in words
    }



words = [
    "apple",
    "banana",
    "orange",
    "grapefruit",
    "pear",
    "kiwi"
]

print(count_words_by_length(words))