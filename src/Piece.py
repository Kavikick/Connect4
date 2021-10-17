"""
    Piece.py

    A representation of a connect4 piece
"""
from dominate.dom_tag import dom_tag


class Piece(dom_tag):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self['cls'] = 'piece'


class WhitePiece(Piece):
    pass


class BlackPiece(Piece):
    pass


class ClearPiece(Piece):
    pass
