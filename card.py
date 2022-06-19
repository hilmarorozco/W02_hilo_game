import random

class Card:
    """Cards that can have a number from 1 to 14.

    The responsibility of Card is to generate a random card number for card one
    and card two.
   
    Attributes:
        card_one (int): The number of card one.
        card_two (int): The number of card two.
    """
    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.card_one = random.randint(1, 13)
        self.card_two = random.randint(1, 13)

    def deal(self):
        """Generates a new card number for card two and gives the number of card
        two to card one.
        
        Args:
            self (Card): An instance of Card.
        """
        self.card_one = self.card_two
        self.card_two = random.randint(1, 13)