from entities.color import Color
from termcolor import colored

class Board:
    # Init board with random colors, set board size and starting cell
    def __init__(self, size):
        self.size = size
        self.board = [[Color.get_random_color() for _ in range(size)] for _ in range(size)] 
        self.start_row = 0
        self.start_col = 0

    # Check if cell is in board bounds
    def in_bounds(self, row, col):
        return row >= 0 and row < self.size and col >= 0 and col < self.size
    
    # Check if Should replace cell color with new one, and spreads for all it's neighbors  
    def set_cell_color(self, row, col, old_color, new_color):

        if not self.in_bounds(row, col):
            return
        
        # Continue just if cell has the replacment color 
        if self.board[row][col] == old_color:

            # Set cell to new color
            self.board[row][col] = new_color

            # spreads for all it's neighbors (up, down, left, right) 
            self.set_cell_color(row - 1, col, old_color, new_color)
            self.set_cell_color(row + 1, col, old_color, new_color)
            self.set_cell_color(row, col - 1, old_color, new_color)
            self.set_cell_color(row, col + 1, old_color, new_color)

    # Set new color from starting cell and spreads for all it's neighbors
    def set_color(self, new_color):
        
        old_color = self.board[self.start_row][self.start_col]
        
        # If starting cell has the same color as the new one, do nothing
        if old_color == new_color:
            return
        else:
            # Replace to new color and spreads for all it's neighbors
            self.set_cell_color(self.start_row, self.start_col, old_color, new_color)

    # Check if all the board is in the same color
    def has_won(self):
        first_color = self.board[self.start_row][self.start_col]
        return all(cell == first_color for row in self.board for cell in row)
    
    # Print all board by coloring boxes
    def print_board(self):
        for row in self.board:
            print(" ".join(colored('■', Color.get_color_by_char(cell)) for cell in row))
