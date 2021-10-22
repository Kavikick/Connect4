"""
    Connect4.py

    Contains the connect4 game
    It ultimately returns html to the FrontEnd
"""
from src.Board import Board
from dominate.tags import *


class Connect4:
    def __init__(self) -> None:
        self.board = Board()
        self.players = []
        self.status = 'in progress'
        self.scoreBoard = div("black's turn", id='ScoreBoard')
        self.nextTurn = 'black'

    def place(self, player, x, y):
        if (self.status != 'won' and player == self.nextTurn):
            self.board.place(player, x, y)
            if self.board.checkIfWon(player, x, y) and self.status == 'in progress':
                self.scoreBoard.children[0] = "{} won!".format(player)
                self.scoreBoard.add(button('new game',
                                           onclick='reset()', id='reset'))
                self.status = 'won'
            elif self.nextTurn == 'black':
                self.nextTurn = 'red'
                self.scoreBoard.children[0] = "{}'s turn".format(self.nextTurn)
            else:
                self.nextTurn = 'black'
                self.scoreBoard.children[0] = "{}'s turn".format(self.nextTurn)

    def display(self):
        return '<div id="Game">'+self.board.render()+'</div>'+self.getScore()

    def getScore(self):
        return self.scoreBoard.render()

    def newGame(self):
        self.board = Board()
        self.status = 'in progress'
        self.scoreBoard.children.pop()
