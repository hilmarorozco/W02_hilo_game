

class Calculate_score:

    def __init__(self):
        self.values = []
        self.player_score = 300

    def calculate_score(card_one, card_two, hilo_answer, player_score):
        
        if (card_one > card_two):
            if (hilo_answer.lower() == "l"):
                player_score = player_score + 100
            else:
                player_score = player_score - 75

        elif (card_one < card_two):
            if (hilo_answer.lower() == "h"):
                player_score = player_score + 100
            else:
                player_score = player_score - 75
        else:
            player_score = player_score + 0
    
        values = [card_one, card_two, hilo_answer, player_score]
    
        return values