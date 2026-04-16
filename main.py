# main.py

from game.game import connect_four_game
from game import minimax
import time


def get_human_move(game, current_player):
    legal = game.legal_moves()

    while True:
        raw = input(
            f"\nPlayer {current_player}, choose a column (0–6): "
        ).strip()

        if raw.isdigit():
            move = int(raw)

            if move in legal:
                return move

        print("Illegal move, try again.")


def choose_difficulty():
    while True:

        print("\nSelect Difficulty:")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            return 3
        elif choice == "2":
            return 5
        elif choice == "3":
            return 7
        else:
            print("Invalid selection. Try again.")


def run_connect_four():

    game = connect_four_game()
    current_player = 1

    print("\nWelcome to Connect Four!")
    print("You are Player 1 (Red). AI is Player 2 (Yellow).")

    ai_depth = choose_difficulty()

    while True:

        print("\n")
        game.print_board()

        if current_player == 1:

            move = get_human_move(
                game,
                current_player
            )

        else:

            print("\nAI is thinking...")
            time.sleep(1)

            move = minimax.best_move(
                game,
                ai_depth
            )

        game.apply_move(
            move,
            current_player
        )

        if game.check_win(current_player):

            game.print_board()

            if current_player == 1:
                print("\nYou win!")
            else:
                print("\nAI wins!")

            break

        if game.is_draw():

            game.print_board()
            print("\nIt's a draw!")

            break

        current_player = (
            2 if current_player == 1 else 1
        )


if __name__ == "__main__":
    run_connect_four()