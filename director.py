from card import Card
from calculate_score import Calculate_score


#card = Card()

class Director:
    
    def __init__(self):
        #self.play = ""
        self.is_playing = True
        #self.score = 0
        #self.total_score = 0

    def start_game(self, player_score):

        while self.is_playing != False:
            self.display()
           
            #self.do_updates()
            #self.scores()
            
    

    # def do_updates(self):
    #     if not self.is_playing:
    #         return



    def display(self, card_one, card_two, hilo_answer, player_score, scores):
        
        print(f'The card is: {card_one}')
        hilo_answer = input("Higher or lower? [h/l] ")
        

        # card_place_holder = Card()
        # card.deal()
        # card_two = card_place_holder.card_two
        # print(f'Next card: {card_two}')
        # numbers = scores(card_one, card_two, hilo_answer, player_score)
        # card_one = numbers[0]
        # card_two = numbers[1]
        # hilo_answer = numbers[2]
        # player_score = numbers[3]
        
        # print(f'Your score is: {player_score}')
        

        

        


