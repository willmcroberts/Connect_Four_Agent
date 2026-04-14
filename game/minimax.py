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

def minimax(game, depth, alpha, beta, maximizing_player):

    legal_moves = game.legal_moves()
    terminal = check_terminal(game)

    if depth == 0 or terminal:
        if terminal:
            if game.check_win(MINNIE_MAXWELL):
                return None, 1000000000
            elif game.check_win(PLAYER):
                return None, -1000000000
            else:
                return None, 0
        else:
            return None, score_position(game, MINNIE_MAXWELL)

    if maximizing_player:
        value = -math.inf
        best_column = random.choice(legal_moves)

        for col in legal_moves:
            new_game = game.copy()
            new_game.apply_move(col, MINNIE_MAXWELL)

            new_score = minimax(new_game, depth - 1, alpha, beta, False)[1]

            alpha = max(alpha, value)

            if alpha >= beta:
                break
        return best_column, value
    else:
        value = math.inf
        best_column = random.choice(legal_moves)

        for col in legal_moves:
            new_game = game.copy()
            new_game.apply_move(col, PLAYER)

            new_score = minimax(new_game, depth - 1, alpha, beta, True)[1]

            if new_score < value:
                value = new_score
                best_column = col

            beta = min(beta, value)

            if alpha >= beta:
                break
        return best_column, value