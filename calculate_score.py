

class Calculate_score:

    def __init__(self):
        self.player_score = 300

    def calculate_score(self, card_both_cards, hilo_answer):
        
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
    
        #return self.player_score


# if __name__ == "__main__":
#     calculate = Calculate_score()
