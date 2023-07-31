# link: https://platzi.com/clases/7967-python-21-dias/63516-filtra-mensajes-de-un-user-especifico/

def filter_user_messages(messages, user):
    return list((filter(lambda x: x['sender']== user, messages)))



messages = [
    {'sender': 'Alice', 'content': 'Hola, ¿cómo estás?'},
    {'sender': 'Bob', 'content': '¡Bien, gracias!'},
    {'sender': 'Alice', 'content': '¿Quieres tomar un café?'},
    {'sender': 'Charlie', 'content': 'Hola a todos.'},
    {'sender': 'Alice', 'content': 'Nos vemos luego.'}
    ]

user = 'Alice'
print(filter_user_messages(messages, user))