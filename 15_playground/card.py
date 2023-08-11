from pay import Pay

class Card(Pay):
    def __init__(self, card_number):
        self.card_number = card_number

    def make_pay(self, quantity):
        if len(self.card_number) != 16:
            raise Exception
        
        return super().make_pay(quantity) | {
            "last_card_numbers": self.card_number[-4:]
        }