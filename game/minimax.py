# minimax.py

import math
import random

MINNIE_MAXWELL = 2
PLAYER = 1
MAX_DEPTH = 4

def scoring(window, player):
    score = 0
    opponent = PLAYER if player == MINNIE_MAXWELL else MINNIE_MAXWELL

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2
    if window.count(opponent) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score_position(game, player):
    board = game.board
    score = 0

    center_column = [board[r][3] for r in range(6)]
    score += center_column.count(player) * 3
    # The center column is the best position on the board, because it allows for the most winning moves

    for c in range(7):
        column_array = [board[r][c] for r in range(6)]

        for r in range(3):
            window = column_array[r:r + 4]
            score += scoring(window, player)

        for r in range(3):
            for c in range(4):
                window = [board[r + i][c + i] for i in range(4)]
                score += scoring(window, player)
        for r in range(3):
            for c in range(3,7):
                window = [board[r+i][c-i] for i in range(4)]
                score += scoring(window, player)
        return score
    return None

def check_terminal(game):
    return (
        game.check_win(MINNIE_MAXWELL) or
        game.check_win(PLAYER) or
        game.is_draw()
    )