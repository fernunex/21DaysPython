# https://platzi.com/clases/7967-python-21-dias/63520-crea-un-auto-usando-clases/

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage
        self.state = False
    
    def turnOn(self):
        self.state = True
    
    def turnOff(self):
        self.state = False

    def drive(self, kilometers):
        if not self.state:
            raise Exception("El auto está apagado")
        else:
            self.mileage += kilometers

# toyota = Car("Toyota", "Corolla", 2020, 50);
# toyota.drive(100);
# print(toyota.mileage)