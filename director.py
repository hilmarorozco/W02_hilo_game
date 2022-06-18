from card import Card

card = Card()

class Director:
    
    def __init__(self):
        self.play = ""
        self.is_playing = True
        self.score = 0
        self.total_score = 0

    def play_game(self):
        self.player_score = 300

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.scores()
            self.do_outputs()
    
    def get_inputs(self):
        hilo_answer = input("High or Low? [h/l]")
        #self.is_playing = (hilo_answer == "h")

    def do_updates(self):
        if not self.is_playing:
            return

    def scores(card_one, card_two, hilo_answer, player_score):
        
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
    
    cardsandscores = [card1num, card2num, hilochoice, player_score, player_luck]
    ## Returns a list of all needed answers
    return cardsandscores



    def do_outputs(self):
        
        if not self.is_playing:
            return
        


