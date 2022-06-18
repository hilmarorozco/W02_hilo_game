import random

class Card:
    def __init__(self):
        self.card_one_num = random.randint(1, 13)
        self.card_two_num = random.randint(1, 13)

    def draw_card(self):
        self.card_two_num = self.card_one_num
        self.card_one_num = random.randint(1, 13)

    
