#https://platzi.com/clases/7967-python-21-dias/63524-playground-implementa-un-sistema-de-pagos/

from card import Card
from paypal import PayPal
from cash import Cash
from pay import Pay

def process_pay(payment_method: Pay, amount):
    return payment_method.make_pay(amount)


if __name__ == '__main__':
    card = Card("4913478952471122")
    print(process_pay(card, 100))

    print("**"*10)
    paypal = PayPal("test@mail.com")
    print(process_pay(paypal, 240))

    print("**"*10)
    cash = Cash()
    print(process_pay(cash, 400))