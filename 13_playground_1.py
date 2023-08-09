from product import Product

class Article(Product):
    def addToCart(self):
        return f"Agregando {self.quantity} unidades del artículo {self.name} al carrito"
    
class Service(Product):
    def addToCart(self):
        return f"Agregando el servicio {self.name} al carrito"
    
class Cart:
    def __init__(self):
        self.lista = []
    
    def addProduct(self, product: Product):
        self.lista.append(product)
        product.addToCart()
    
    def deleteProduct(self, product):
        self.lista.remove(product)
    
    def calculateTotal(self):
        return sum(product.price * product.quantity for product in self.lista)
    
    def getProducts(self):
        return self.lista
    
if __name__ == '__main__':
    # book = Article("Libro", 100, 2);
    # course = Service("Curso", 120, 1);

    # cart = Cart();
    # print(cart.addProduct(book))
    # print(cart.addProduct(course))
    # print(cart.calculateTotal())
    # print(cart.getProducts())

    book = Article("Libro", 100, 2);
    course = Service("Curso", 120, 1);

    cart = Cart();
    print(cart.addProduct(book))
    print(cart.addProduct(course))
    print(cart.deleteProduct(book))
    print(cart.calculateTotal())
