"""
    Board.py

    A dynamically sized game board
"""
from dominate.tags import *
from src.Piece import *


class Board:
    def __init__(self, width=7, height=6):
        self.width = width
        self.height = height
        self.table = table()
        with self.table:
            for w in range(width):
                row = tr()
                with row:
                    for h in range(height):
                        td(Piece(onclick='update('+str(w)+','+str(h)+');'))

    def render(self):
        return self.table.render()

    def place(self, color, x, y):
        # adjust y cord to account for gravity and existing pieces
        slot = 0
        while slot < self.height:
            if self.table.children[x][slot][0]['class'] == 'clearpiece':
                y = slot
                break
            slot += 1
            print(slot)
        if color == "RED":
            self.table.children[x][y][0]['class'] = 'redpiece'
        elif color == "BLACK":
            pass

    def checkIfWon(self):
        # Evaluate if the game has been won
        # Sum the up and down neighbors in a line
        # Sum the UpperRight to LowerLeft in a line
        # Sum the UL to LR in a line
        # If any of those add up to 4 the color won
        return True
