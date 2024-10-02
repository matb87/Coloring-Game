# Coloring-Game

Game Rules:

* The game has a board that is 18x18 and is initialized randomly with 4 colors. 
* In each turn, the player must choose a color and type it in (red (r), blue (b), green (g), yellow (y)).
* The top left cell is the "starting cell".
* The new color (that the player chose) spreads to all of the starting cell's neighbors' sequence which have the same color as it does. 
* A "neighbor" is an adjacent cell either up, down, left, or right from the cell itself. 
* This happens every turn until the player either wins or loses the game.
* To win, the board must be of one color and at a maximum of 21 moves. 
* The player loses if after 21 moves the board is not colored in a single color.

Setup:
* Please install termcolor package
* Run main.py to start playing