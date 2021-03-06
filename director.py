from card import Card
from calculate_score import Calculate_score

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        is_playing (boolean): Whether or not the game is being played.
        want_to_play (string): Whether the player wants to keep playing or not.
        hilo_answer (string): Whether the player thinks the second card is higher or lower.
        score (int): The player's score.      
    """
    
    def __init__(self):
        """Constructs a new instance of Director.

        Args:
            self (Director): An instance of Director.
        """
        self.is_playing = True

    def play_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        # new instance of a card
        card_both_cards = Card()
        score = Calculate_score()

        while self.is_playing != False:
            want_to_play = input("\nDo you want to play? [y/n] ")
            
            if want_to_play.lower() == "y":
                print(f"Card number one is {card_both_cards.card_one}")
                hilo_answer = input("Higher or lower? [h/l] ")
                print(f"Card number two is {card_both_cards.card_two}")
                score.calculate_score(card_both_cards, hilo_answer)
                
                if score.player_score <= 0:
                    print("Oh no! You ran out of points.")
                    return
                
                print(f"Your current points are {score.player_score}.")
                card_both_cards.deal()
                                
            else:
                self.is_playing = False