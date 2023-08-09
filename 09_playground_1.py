# https://platzi.com/clases/7967-python-21-dias/63518-maneja-correctamente-los-errores/

def calculate_average(numbers):
    
    if len(numbers) == 0:
        raise ValueError("La lista está vacía")
    
    for i in numbers:
        if type(i) == str or type(i) == bool:
            raise TypeError("La lista contiene elementos no numéricos")
    else:
        return sum(numbers)/len(numbers)

    

print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([10, 20, 30, 40, 50]))
# print(calculate_average([]))
print(calculate_average([1, 2, '3', 4, 5]))


# Input: calculate_average([1, 2, 3, 4, 5])
# Output: 3.0

# Input: calculate_average([10, 20, 30, 40, 50])
# Output: 30.0


# Input: calculate_average([])
# Output: ValueError: La lista está vacía


# Input: calculate_average([1, 2, '3', 4, 5])
# Output: TypeError: La lista contiene elementos no numéricos