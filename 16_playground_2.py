# https://platzi.com/clases/7967-python-21-dias/63709-playground-implementacion-de-una-hashtable-para-co/

class ContactList:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for x in range(size)]
    
    def hash(self, key):
        return hash(key) % self.size

    def insert(self, name, phone):
        """este método recibirá el nombre y el número de teléfono 
        de un contacto y agregará este último a la hash table."""
        index = self.hash(name)
        self.buckets[index].append((name, phone))


    def get(self, name):
        """este método recibirá el nombre de un contacto y devolverá 
        su número de teléfono. Si el contacto no existe, retornará None"""
        index = self.hash(name)
        for name_key, phone in self.buckets[index]:
            if name_key == name:
                return phone
        return None

    def retrieveAll(self):
        """este método devolverá una lista con todos los buckets utilizados 
        en la hash table."""
        all_buckets = []
        for bucket in self.buckets:
            if bucket:
                for bucket_single in bucket:
                    all_buckets.append([bucket_single[0], bucket_single[1]])
        return all_buckets


    def delete(self, name):
        """delete(name): este método recibirá el nombre de un contacto y eliminará 
        dicho contacto de la hash table. En caso de no encontrar el nombre, debe retornar None."""
        index = self.hash(name)
        for i, (name_key, phone) in enumerate(self.buckets[index]):
            if name_key == name:
                print(name_key)
                print(phone)
                del self.buckets[index][i]
                return
        return None
        

if __name__ == '__main__':
    contactList = ContactList(10)
    contactList.insert("Mr michi", "123-456-7890")
    print(contactList.buckets)
    print(contactList.get("Mr michi"))   
    print(contactList.retrieveAll())
    print(contactList.delete("Mr michi"))
    print(contactList.buckets)

    # print(contactList.size)
    # print(contactList.hash('mr michi'))

    # contactList.retrieveAll()