import os
from entities.board import Board
from entities.player import Player
from entities.color import Color


class ColoringGame:
    def __init__(self, board_size, max_moves, player_name):
        self.board = Board(board_size)
        self.player = Player(player_name)
        self.max_moves = max_moves
        self.left_moves = max_moves

    # Print Game instructions
    def print_instructions(self):
        print(f"Hello {self.player.name}!")
        print(f"You have {self.max_moves} moves.")
        print(f"In each move you choose a color from the options ({Color.get_color_options()}).")
        print(f"The selected color will change the board from the starting cell [{self.board.start_row}, {self.board.start_row}],")
        print("Spreads to all the neighbors of the starting cell which have the same color.")
        print("Your goal is to make the entire board the same color.")
        print("Good Luck!")
        input("Enter any key to start...")
        os.system('cls')

    # Game playing structure
    def play(self):
        self.print_instructions()
        
        # Continue playing until the player wins or he out of moves
        while self.left_moves > 0 and self.board.has_won() == False:
            # Show the board state
            self.board.print_board()

            # Getting next move
            print(f"Moves Left: {self.left_moves}.")
            move = self.player.get_move()

            # Apply new color on board
            self.board.set_color(move)

            # Reducing the amount of moves
            self.left_moves -= 1

            # resest screen
            os.system('cls')
        
        # Print the Final board
        self.board.print_board()

        # Tell the player if he won or lost
        if self.board.has_won():
            print(f"Great job {self.player.name}, You won the game!!!")
        else:
            print(f"You lost, Maybe next time")