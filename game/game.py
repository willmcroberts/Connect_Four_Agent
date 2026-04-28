# game.py

class connect_four_game:

    def __init__(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]

    def legal_moves(self):
        return [c for c in range(7) if self.board[0][c] == 0]

    def apply_move(self, column, player):
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = player
                return row, column
        raise ValueError("Column is full")

    def check_win(self, player):
        # Check horizontal
        for r in range(6):
            for c in range(4):
                if all(self.board[r][c+i] == player for i in range(4)):
                    return True

        # Check vertical
        for r in range(3):
            for c in range(7):
                if all(self.board[r+i][c] == player for i in range(4)):
                    return True

        # Check diagonals
        for r in range(3):
            for c in range(4):
                if all(self.board[r+i][c+i] == player for i in range(4)):
                    return True

        for r in range(3):
            for c in range(3,7):
                if all(self.board[r+i][c-i] == player for i in range(4)):
                    return True

        return False

    def is_draw(self):
        return len(self.legal_moves()) == 0

    def copy(self):
        new_env = connect_four_game()
        new_env.board = [row[:] for row in self.board]
        return new_env

    # For CLI testing
    def print_board(self):
        RESET = "\033[0m"
        RED = "\033[91m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"

        def color(cell):
            if cell == 1:
                return RED + "R" + RESET
            elif cell == 2:
                return YELLOW + "Y" + RESET
            else:
                return BLUE + "." + RESET

        for row in self.board:
            print(" ".join(color(c) for c in row))

        print("0 1 2 3 4 5 6")