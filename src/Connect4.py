"""
    Connect4.py

    Contains the connect4 game
    It ultimately returns html to the FrontEnd
"""
from Board import Board


class Connect4:
    def __init__(self) -> None:
        self.board = Board()
        self.players = []
        pass

    def place(self, player, x, y):
        # Check if it's the player's turn
        # place the piece and if the board says the game is won then player wins
        pass

    def display(self):
        return '<div id="Game">'+self.board.print()+'</div>'+self.getScore()

    def getScore(self):
        return '<div id="ScoreBoard"></div>'

    def newGame(self, width, height):
        self.board = Board(width, height)
