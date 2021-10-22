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
                        td(Piece(), onclick='update('+str(w)+','+str(h)+');')

    def render(self):
        return self.table.render()

    def getSlot(self, x, y):
        # Check if it's a legal piece
        if x >= 0 and x < self.width and y >= 0 and y < self.height:
            return self.table.children[x][y]
        else:
            return None

    def place(self, color, x, y):
        # adjust y cord to account for gravity and existing pieces
        slot = 0
        while slot < self.height:
            if self.getSlot(x, slot)[0]['class'] == 'clearpiece':
                y = slot
                break
            slot += 1
            if slot == self.height:  # Breaking point in case the collumn is full
                return False
        if color == "red":
            self.getSlot(x, y)[0]['class'] = 'redpiece'
        elif color == "black":
            self.getSlot(x, y)[0]['class'] = 'blackpiece'

        return True  # A piece did get placed

    def sumLine(self, color, sweep, translator):
        chainLength = 0
        longestChain = 0
        for val in sweep:
            x, y = translator(val)
            slot = self.getSlot(x, y)
            if not slot or slot[0]['class'] != color+'piece':
                chainLength = 0
            else:
                chainLength += 1
                if chainLength > longestChain:
                    longestChain = chainLength
        return longestChain

    def checkIfWon(self, color, x, y):
        counts = []
        # Vertical (y-3 to y+4)
        counts.append(self.sumLine(color, range(y-3, y+4),
                      translator=lambda val: (x, val)))

        # Horizontal (x-3 to x+4)
        counts.append(self.sumLine(color, range(x-3, x+4),
                      translator=lambda val: (val, y)))

        # Sum the LowerLeft to UpperRight in a line (x-3 to x+4)
        slope, intercept = (1, -x+y)
        counts.append(self.sumLine(color, range(x-3, x+4),
                      translator=lambda val: (val, slope*val+intercept)))
        # Sum the UL to LR in a line (x-3 to x+4)
        slope, intercept = (-1, x+y)
        counts.append(self.sumLine(color, range(x-3, x+4),
                      translator=lambda val: (val, slope*val+intercept)))

        # If any of those add up to 4 the color won
        for sum in counts:
            if sum >= 4:
                return True
        return False
