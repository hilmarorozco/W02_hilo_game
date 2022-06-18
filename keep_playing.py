

class Keep_playing:
    def __init__(self):
        
        
        if player_score > 0:
            play_again = input("Do you want to play again? [y/n] ")
            if play_again.lower() == "n":
                self.is_playing = False
        else:
            self.is_playing = False