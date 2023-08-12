# https://platzi.com/clases/7967-python-21-dias/63843-playground-implementacion-de-una-queue/

from mail import Mail

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, from_email, to, body, subject):
        """Agrega un correo electrónico al final de la cola."""
        new_email = Mail(from_email, to, body, subject)
        if self.first is None:
            self.first = new_email
            self.last = new_email
        else:
            self.last.next = new_email
            self.last = new_email
        self.length += 1


    def dequeue(self):
        """Elimina y devuelve un objeto con las siguientes propiedades: { from_email, to, body, subject } del correo electrónico más antiguo de la cola.
        pdt: Existe una inconsistencia en la explicacion del playground"""
        if self.length == 0:
            raise IndexError("No hay emails.")

        dequeue_email = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        # return{
        #     "from_email": dequeue_email.from_email,
        #     "to": dequeue_email.to,
        #     "body": dequeue_email.body,
        #     "subject": dequeue_email.subject,
        # }
        return dequeue_email
    
    def peek(self):
        """Devuelve el correo electrónico más antiguo de la cola sin eliminarlo.
        pdt: Existe una inconsistencia en la explicacion del playground"""
        # return{
        #     'from_email': self.first.from_email,
        #     "to": self.first.to,
        #     "body": self.first.body,
        #     "subject": self.first.subject,
        # }
        return self.first 

    def is_empty(self):
        """Retorna True si length es 0, False otherwise."""
        return self.length == 0
    
    def size(self):
        """Devuelve la cantidad de correos electrónicos en la cola."""
        return self.length



if __name__ == '__main__':
    emailQueue = Queue()

    emailQueue.enqueue(
        'jane@ejemplo.com',
        'support@ejemplo.com',
        'No puedo iniciar sesión en mi cuenta',
        'Problema de inicio de sesión'
    )

    emailQueue.enqueue(
        'joe@ejemplo.com',
        'support@ejemplo.com',
        'Mi pedido no ha llegado todavía',
        'Estado del pedido'
    )

    print(emailQueue.peek())
    email = emailQueue.dequeue()
    print(email)
    # print(emailQueue.first.subject)
    # print(emailQueue.first.next.subject)
    