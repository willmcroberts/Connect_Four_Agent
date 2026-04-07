# game.py

from . import minimax

class connect_four:

    self.board = [[0 for _ in range(7)] for _ in range(6)]

    def legal_moves(self):
        return [c for c in range(7) if self.board[0][c] == 0]

