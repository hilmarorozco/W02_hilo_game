class Calculate_score:
    """A calculator for the player's points.

    The responsibility of Calculate_score to keep track of the player's points, 
    by subtracting and adding according if the user got it right or wrong.
   
    Attributes:
        player_score (int): The initial points that the player starts with (300 points).
    """
    def __init__(self):
        """Constructs a new instance of Calculate_score.

        Args:
            self (Calculate_score): An instance of Calculate_score.
        """
        self.player_score = 300

    def calculate_score(self, card_both_cards, hilo_answer):
        """Calculates the player's score based on performance.
        If the player guesses correctly, the player receives 100 points,
        however if the player fails to guess it correctly, he losses 75 points.
        
        Args:
            self (Calculate_score): An instance of Calculate_score.
            card_both_cards(Card): An instance of Card.
            hilo_answer(Director): An instance of Director.
        """
        
        if (card_both_cards.card_one > card_both_cards.card_two):
            if (hilo_answer.lower() == "l"):
                self.player_score = self.player_score + 100
            else:
                self.player_score = self.player_score - 75

        elif (card_both_cards.card_one < card_both_cards.card_two):
            if (hilo_answer.lower() == "h"):
                self.player_score = self.player_score + 100
            else:
                self.player_score = self.player_score - 75
        else:
            self.player_score = self.player_score + 0

# if __name__ == "__main__":
#     calculate = Calculate_score()
