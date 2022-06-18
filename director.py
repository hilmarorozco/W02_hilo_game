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
            self.do_updates()
            self.scores()
            self.display()
    

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
    
        numbers = [card_one, card_two, hilo_answer, player_score]
    
        return numbers

    def display(self, card_one, card_two, hilo_answer, player_score, scores):
        
        while self.is_playing != False:
            
            print(f'The card is: {card_one}')
            hilo_answer = input("Higher or lower? [h/l] ")
            card_place_holder = Card()
            card.deal()
            card_two = card_place_holder.card_two
            print(f'Next card: {card_two}')
            numbers = scores(card_one, card_two, hilo_answer, player_score)
            card_one = numbers[0]
            card_two = numbers[1]
            hilo_answer = numbers[2]
            player_score = numbers[3]
            
            print(f'Your score is: {player_score}')
            
            if player_score > 0:
                play_again = input('Play again? [y/n] ')
                if play_again.lower() == 'y':
                    card_one = card_two
                else:
                    self.is_playing = False
            else:
                self.is_playing = False
        

        


