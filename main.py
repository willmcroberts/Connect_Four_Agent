# main.py

from game.game import connect_four_game

def run_connect_four():
    game = connect_four_game()
    current_player = 1

    while True:
        print("\n")
        game.print_board()

        legal = game.legal_moves()

        while True:
            raw = input(f"\nPlayer {current_player}, choose a column: ").strip()
            if raw.isdigit():
                move = int(raw)
                break
            print("Please enter a number between 0 and 6.")

        if move not in legal:
            print("Illegal move, try again.")
            continue

        game.apply_move(move, current_player)

        if game.check_win(current_player):
            game.print_board()
            print(f"\nPlayer {current_player} wins!")
            break

        if game.is_draw():
            game.print_board()
            print("\nIt's a draw!")
            break

        current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    run_connect_four()