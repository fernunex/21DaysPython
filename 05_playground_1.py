
def count_letters(phrase):
    return {letter: phrase.count(letter)
            for letter in phrase}

print(count_letters("Hola mundo"))