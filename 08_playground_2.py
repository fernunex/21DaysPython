# link: https://platzi.com/clases/7967-python-21-dias/63517-crea-tu-propio-metodo-map/

def my_map(list, func):
    return [func(x)
        for x in list]


print(my_map([1, 2, 3, 4], lambda num: num * 2))
print(my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"]))