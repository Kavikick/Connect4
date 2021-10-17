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
                        td(WhitePiece('w'))

    def render(self):
        return self.table.render()

    def isPlayableLocation(self, x, y):
        return True

    def place(self, color, x, y):
        # place the piece
        return None

    def checkIfWon(self):
        # Evaluate if the game has been won
        return True
