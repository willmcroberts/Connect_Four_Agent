import tkinter as tk
from game.game import connect_four_game
from game import minimax

CELL_SIZE = 80
ROWS = 6
COLS = 7


class ConnectFourGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")

        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack()

        self.game = None
        self.depth = 5  # default

        self.show_main_menu()

    def show_main_menu(self):
        self.clear_frame()

        tk.Label(
            self.main_frame,
            text="Connect Four",
            font=("Arial", 32)
        ).pack(pady=20)

        tk.Button(
            self.main_frame,
            text="Play",
            font=("Arial", 20),
            width=10,
            command=self.show_difficulty_menu
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Quit",
            font=("Arial", 20),
            width=10,
            command=self.window.destroy
        ).pack(pady=10)

    def show_difficulty_menu(self):
        self.clear_frame()

        tk.Label(
            self.main_frame,
            text="Select Difficulty",
            font=("Arial", 28)
        ).pack(pady=20)

        tk.Button(
            self.main_frame,
            text="Easy",
            font=("Arial", 20),
            width=10,
            command=lambda: self.start_game(3)
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Medium",
            font=("Arial", 20),
            width=10,
            command=lambda: self.start_game(5)
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Hard",
            font=("Arial", 20),
            width=10,
            command=lambda: self.start_game(7)
        ).pack(pady=10)

        tk.Button(
            self.main_frame,
            text="Back",
            font=("Arial", 16),
            command=self.show_main_menu
        ).pack(pady=20)

    def start_game(self, depth):
        self.depth = depth
        self.game = connect_four_game()

        self.clear_frame()

        self.canvas = tk.Canvas(
            self.main_frame,
            width=COLS * CELL_SIZE,
            height=ROWS * CELL_SIZE,
            bg="blue"
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for r in range(ROWS):
            for c in range(COLS):
                x1 = c * CELL_SIZE + 10
                y1 = r * CELL_SIZE + 10
                x2 = x1 + CELL_SIZE - 20
                y2 = y1 + CELL_SIZE - 20

                cell = self.game.board[r][c]

                if cell == 1:
                    color = "red"
                elif cell == 2:
                    color = "yellow"
                else:
                    color = "white"

                self.canvas.create_oval(x1, y1, x2, y2, fill=color)

    def handle_click(self, event):
        col = event.x // CELL_SIZE

        if col not in self.game.legal_moves():
            return

        self.game.apply_move(col, 1)
        self.draw_board()

        if self.game.check_win(1):
            self.end_game("You win")
            return

        if self.game.is_draw():
            self.end_game("Draw")
            return

        self.window.after(200, self.ai_move)

    def ai_move(self):
        col = minimax.best_move(self.game, self.depth)
        self.game.apply_move(col, 2)
        self.draw_board()

        if self.game.check_win(2):
            self.end_game("AI wins")
        elif self.game.is_draw():
            self.end_game("Draw")

    def end_game(self, message):
        popup = tk.Toplevel(self.window)
        popup.title("Game Over")

        tk.Label(popup, text=message, font=("Arial", 16)).pack(pady=10)
        tk.Button(popup, text="Play Again", command=lambda: [popup.destroy(), self.show_difficulty_menu()]).pack(pady=5)
        tk.Button(popup, text="Main Menu", command=lambda: [popup.destroy(), self.show_main_menu()]).pack(pady=5)
        tk.Button(popup, text="Quit", command=self.window.destroy).pack(pady=5)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def run(self):
        self.window.mainloop()
