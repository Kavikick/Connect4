"""
    Board.py

    A dynamically sized game board
"""
from dominate.tags import *


class Board:
    def __init__(self, width=7, height=6) -> None:
        self.width = width
        self.height = height
        self.turn = "Black"
        # create game board

    def isPlayableLocation(self, x, y):
        return True

    def place(self, color, x, y):
        # place the piece
        return None

    def checkIfWon(self):
        # Evaluate if the game has been won
        return True

    def print(self):
        return h1('Hello, World').render()
