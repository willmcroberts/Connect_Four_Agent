# game.py

from . import minimax

class connect_four:

    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]

    def legal_moves(self):
        return [c for c in range(7) if self.board[0][c] == 0]

    def apply_move(self, column, player):
        for row in range(5, -1, -1):
            if self.board[row][column] ==0:
                self.board[row][column] = player
                return row, column
        raise ValueError("Column is full")

    def check_win(self, player):
        print()

    def is_draw(self):
        print()

    def copy(self):
        print()

    def print_board(self):
        print()