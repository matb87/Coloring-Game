from entities.coloring_game import ColoringGame
import os

def play_game():

    print("Welcome to the Colored Game!")

    # Get player name
    player_name = input("Whats your name? ")
    os.system('cls')

    # Init game settings and Start playing
    color_game = ColoringGame(18, 21, player_name)
    color_game.play()

if __name__ == "__main__":
    play_game()
    
