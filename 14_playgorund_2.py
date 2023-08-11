#https://platzi.com/clases/7967-python-21-dias/63523-playground-jerarquia-de-animales-usando-herencia/

class Animal:
    def __init__(self, name, age, specie):
        self.name = name
        self.age = age
        self.specie = specie

    def getInfo(self):
        return {
            'name': self.name,
            'age': self.age,
            'specie': self.specie
        }
        

class Mammal(Animal):
    def __init__(self, name, age, specie, hasFur):
        super().__init__(name, age, specie)
        self.hasFur = hasFur

    def getInfo(self):
        return super().getInfo() | {'hasFur': self.hasFur}

class Dog(Mammal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, specie = 'dog', hasFur = True)
        self.breed = breed

    def getInfo(self):
        return super().getInfo() | {'breed': self.breed}
    
    def bark(self):
        return 'woof!'
        

if __name__ == '__main__':
    bird = Animal("pepe", 1, "bird")
    print(bird.getInfo())

    print("*"*20)
    hippo = Mammal("bartolo", 3, "hippo", False)
    print(hippo.getInfo())

    print("*"*20)
    dog = Dog("fido", 4, "pastor aleman");
    print(dog.getInfo())
    dog.bark()