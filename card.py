import random

class Card:
    def __init__(self):
        self.card_one = random.randint(1, 13)
        self.card_two = random.randint(1, 13)

    def deal(self):
        self.card_one = self.card_two
        self.card_two = random.randint(1, 13)

    
