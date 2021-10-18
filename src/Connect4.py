"""
    Connect4.py

    Contains the connect4 game
    It ultimately returns html to the FrontEnd
"""
from src.Board import Board


class Connect4:
    def __init__(self) -> None:
        self.board = Board()
        self.players = []
        pass

    def place(self, player, x, y):
        self.board.place("red", x, y)
        pass

    def display(self):
        return '<div id="Game">'+self.board.render()+'</div>'+self.getScore()

    def getScore(self):
        return '<div id="ScoreBoard"></div>'

    def newGame(self):
        self.board = Board()
