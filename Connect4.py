"""
    Connect4.py

    Contains the connect4 game
    It ultimately returns html to the FrontEnd
"""


class Piece:
    def __init__(self, color) -> None:
        self.color = color


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.wins = 0
        self.games = 0
        pass

    def IWon(self):
        self.games += 1
        self.wins += 1

    # Counts for both losses and draws
    def ILost(self):
        self.games += 1

    def getWins(self):
        return self.wins

    def getGames(self):
        return self.games

    def getLosses(self):
        return self.games - self.wins


class Board:
    def __init__(self, width, height) -> None:
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
        return "<p>Hehe I'm not working yet</p>"


class Connect4:
    def __init__(self) -> None:
        self.board = Board(4, 5)
        self.players = []
        pass

    def place(self, player, x, y):
        # Check if it's the player's turn
        pass

    def registerPlayer(self, player):
        self.players.append(Player(player))

    def display(self):
        return '<div id="Game">'+self.board.print()+self.getScore()+'</div>'

    def getScore(self):
        return '</div><div id="ScoreBoard">'

    def newGame(self, width, height):
        self.board = Board(width, height)
