import random
from termcolor import colored

# All abailable colors 
colors = {
    "y" : "yellow",
    "r" : "red",
    "b" : "blue",
    "g" : "green"
}

class Color():

    # Get a random color from colors list
    def get_random_color():
        return random.choice(list(colors.keys()))
    
    # Check if color exists in the list
    def exists(color):
        return color in colors.keys()
    
    # Get color name by first char, return None if not available
    def get_color_by_char(char):
        if Color.exists(char):
            return colors[char]
        else:
            return None

    # Get all the colors options to choose from as format string     
    def get_color_options():
        return ", ".join(f"{colored(key, val)} for {colored(val, val)}" for key,val in colors.items())
        
    