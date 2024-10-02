from entities.color import Color

class Player:
    def __init__(self, name):
        self.name = name
    
    # Get player next move of choosing the next color, continue until is a valid color  
    def get_move(self):
        while True:
            move = input(f"Choose a color ({Color.get_color_options()}): ").lower()
            if not Color.exists(move):
                print("Invalid color, please try again")
            else:
                return move 
        