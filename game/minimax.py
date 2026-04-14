# minimax.py

import math
import random

MINNIE_MAXWELL = 2
PLAYER = 1
MAX_DEPTH = 4

def evaluation(window, player):
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