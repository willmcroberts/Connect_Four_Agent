# main.py

from game import connect_four

def run_connect_four():
    game = __name__()
    current_player = 1

    while True:
        print("\nCurrent board:")
        game.print_board()

        legal = game.legal_moves()
        print("Legal moves:", legal)

        move = int(input(f"Player {current_player}, choose a column: "))

        if move not in legal:
            print("Illegal move, try again.")
            continue

        game.apply_move(move, current_player)

        if game.check_win(current_player):
            game.print_board()
            print(f"Player {current_player} wins!")
            break

        if game.is_draw():
            game.print_board()
            print("It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    run_connect_four()