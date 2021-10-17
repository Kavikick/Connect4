"""
    Player.py

    A class meant to contain all the stats about a player
"""


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
