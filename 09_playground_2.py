#https://platzi.com/clases/7967-python-21-dias/63519-maneja-las-excepciones/

def calculate_discounted_price(price, discount):
    
    if type(price) == str or type(discount) == str:
        raise TypeError("El precio y el descuento deben ser números")

    if price < 0 or discount < 0:
        raise ValueError("El precio y el descuento deben ser valores positivos")
    
    try:
        return (1 - discount) * price
    except:
        raise Exception("Ha ocurrido un error inesperado")


print(calculate_discounted_price(100, 0.2))
print(calculate_discounted_price(-50, 0.2))
