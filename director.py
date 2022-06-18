from card import Card
from calculate_score import Calculate_score


#card = Card()

class Director:
    
    def __init__(self):
        self.is_playing = True

    def play_game(self):

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
                    print("You lost.")
                    return
                
                print(f"Your current points are {score.player_score}.")

                card_both_cards.deal()
                                
            else:
                self.is_playing = False



        

        


