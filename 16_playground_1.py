#https://platzi.com/clases/7967-python-21-dias/63708-playground-implementacion-de-una-hashtable-para-co/

class MyList:
    def __init__(self):
        self.data = {}
        self.length = 0

    def _reasignar_keys(self):
        """Re-ordena las keys para que inicien en 0 y terminen en length"""
        new_data = {}
        index = 0

        # If insert item at 0
        if -1 in self.data:
            new_data[0] = self.data.pop(-1)
            index = 1
        
        # if remove item at 0
        for key in self.data:
            new_data[index] = self.data[key]
            index += 1
        self.data = new_data


    def append(self, item):
        """Agrega un elemento item al final de la lista"""
        self.data[self.length] = item
        self.length += 1

    def pop(self):
        """Elimina el último elemento de la lista y lo retorna"""
        val = self.data.pop(self.length - 1)
        self.length -= 1
        return val
        

    def shift(self):
        """Elimina el primer elemento de la lista y lo retorna"""
        val = self.data.pop(0)
        self.length -= 1
        self._reasignar_keys()
        return val

    def unshift(self, item):
        """Agrega un elemento item al inicio de la lista"""
        self.data[-1] = item
        self.length += 1
        self._reasignar_keys()
        

    def map(self, func):
        """ itera sobre cada elemento de nuestra estructura aplicando
        la función func a cada uno de ellos y devuelve una nueva lista 
        (que será una instancia de MyList"""

        new_list = MyList()
        for key in self.data:
            new_list.append(func(self.data[key]))
        return new_list

    def filter(self, func):
        """ itera sobre cada elemento de nuestra estructura filtrándolos 
        según lo que indique la función func y devuelve una lista con los 
        elementos filtrados (también una instancia de MyList)."""

        new_list = MyList()
        for key in self.data:
            if func(self.data[key]):
                new_list.append(self.data[key])
        return new_list

    def join(self, character = ','):
        """concatena todos los elementos de nuestra estructura de datos en 
        un string, separándolos por el carácter indicado (character). Si no 
        se proporciona un carácter, el separador por defecto será una coma ","."""
        string = ''
        for item in self.data.values():
            string += str(item) + character
        return string[:-len(character)]


if __name__ == '__main__':
    # TEST 1
    myList = MyList()
    myList.append("a")
    myList.append("b")
    myList.append("c")

    # print(myList.pop())
    # print(myList.shift())
    # print(myList.join())
    # print(myList.filter(lambda x: x != "a").data)
    # print(myList.map(lambda x: x+'8').data)
    print(myList.join('<3'))
    print(myList.data)
    print(myList.length)

    # TEST 2
    # myList = MyList()
    # myList.append("Platzinauta")
    # myList.unshift("Hola!")

    # print(myList.data)