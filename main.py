from entities.coloring_game import ColoringGame
import os

# Game Settings
game_board_size = 18
game_max_moves = 21

def play_game():

    print("Welcome to the Colored Game!")

    # Get player name
    player_name = input("Whats your name? ")
    os.system('cls')

    # Init game settings and Start playing
    color_game = ColoringGame(game_board_size, game_max_moves, player_name)
    color_game.play()

if __name__ == "__main__":
    play_game()
    
