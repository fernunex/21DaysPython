#https://platzi.com/clases/7967-python-21-dias/63522-playground-encapsula-datos-de-los-usuarios/

class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._friends = []
        self._messages = []

    def addFriend(self, friend):
        self._friends.append(friend)

    def sendMessage(self, message, friend):
        self._messages.append(message)
        friend._messages.append(message)

    def showMessages(self):
        return self._messages
    
    @property
    def name(self):
        return self._name

    @name.setter    
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

if __name__ == '__main__':
    # Test 1
    # usuario1 = User("Juan", 20)
    # usuario2 = User("Maria", 25)
    # usuario1.addFriend(usuario2)
    # usuario1.sendMessage("Hola Maria!", usuario2)

    # print(usuario1.showMessages())
    # print(usuario2.showMessages())

    # TEST 2
    usuario1 = User("Juan", 20)
    print(usuario1.name)
    usuario1.name = "Pepito"
    print(usuario1.name)
    print(usuario1.name)
    print(usuario1.name)
    print(usuario1.name)