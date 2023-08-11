from pay import Pay

class PayPal(Pay):
    def __init__(self, email):
        self.email = email
    
    def make_pay(self, quantity):
        return super().make_pay(quantity) | {
            "platform": "PayPal",
            "email": self.email
        }