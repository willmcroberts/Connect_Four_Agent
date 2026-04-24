import tkinter as tk
from game.game import connect_four_game
from game import minimax

CELL_SIZE = 80
ROWS = 6
COLS = 7

APP_WIDTH = COLS * CELL_SIZE
APP_HEIGHT = ROWS * CELL_SIZE + 60

class ConnectFourGUI:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.window.resizable(False, False)

        self.app_frame = tk.Frame(self.window, width=APP_WIDTH, height=APP_HEIGHT)
        self.app_frame.pack_propagate(False)
        self.app_frame.pack()

        self.current_screen = None
        self.game = None
        self.depth = 5
        self.last_ai_move = None

        self.show_main_menu()

    def switch_screen(self, new_frame):
        if self.current_screen is not None:
            self.current_screen.destroy()

        self.current_screen = new_frame
        self.current_screen.pack(fill="both", expand=True)

    def show_main_menu(self):
        frame = tk.Frame(self.app_frame, bg="#1e1e1e")

        tk.Label(
            frame,
            text="Connect Four",
            font=("Arial", 36, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=40)

        self.make_menu_button(frame, "Play", self.show_difficulty_menu)
        self.make_menu_button(frame, "Quit", self.window.destroy)

        self.switch_screen(frame)

    def show_difficulty_menu(self):
        frame = tk.Frame(self.app_frame, bg="#1e1e1e")

        tk.Label(
            frame,
            text="Select Difficulty",
            font=("Arial", 28, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=40)

        self.make_menu_button(frame, "Easy", lambda: self.start_game(3))
        self.make_menu_button(frame, "Medium", lambda: self.start_game(5))
        self.make_menu_button(frame, "Hard", lambda: self.start_game(7))

        self.make_menu_button(frame, "Back", self.show_main_menu, small=True)

        self.switch_screen(frame)

    def start_game(self, depth):
        self.depth = depth
        self.game = connect_four_game()
        self.last_ai_move = None

        frame = tk.Frame(self.app_frame, bg="blue")

        self.turn_label = tk.Label(
            frame,
            text="Your Turn (Red)",
            font=("Arial", 20, "bold"),
            bg="blue",
            fg="white"
        )
        self.turn_label.pack(pady=5)

        self.canvas = tk.Canvas(
            frame,
            width=APP_WIDTH,
            height=APP_HEIGHT - 60,
            bg="blue",
            highlightthickness=0
        )
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.handle_click)

        self.switch_screen(frame)
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

                if self.last_ai_move == (r, c):
                    self.canvas.create_oval(
                        x1 - 4, y1 - 4, x2 + 4, y2 + 4,
                        outline="black",
                        width=4
                    )

    def handle_click(self, event):
        col = event.x // CELL_SIZE

        if col not in self.game.legal_moves():
            return

        self.game.apply_move(col, 1)
        self.last_ai_move = None
        self.draw_board()

        if self.game.check_win(1):
            self.show_end_screen("You win!")
            return

        if self.game.is_draw():
            self.show_end_screen("It's a draw!")
            return

        self.turn_label.config(text="AI Thinking...", fg="yellow")

        self.window.after(500, self.ai_move)

    def ai_move(self):
        col = minimax.best_move(self.game, self.depth)
        row, col = self.game.apply_move(col, 2)
        self.last_ai_move = (row, col)

        self.draw_board()

        if self.game.check_win(2):
            self.show_end_screen("AI wins!")
            return

        if self.game.is_draw():
            self.show_end_screen("It's a draw!")
            return

        # Back to human turn
        self.turn_label.config(text="Your Turn (Red)", fg="white")

    def show_end_screen(self, message):
        frame = tk.Frame(self.app_frame, bg="#1e1e1e")

        tk.Label(
            frame,
            text=message,
            font=("Arial", 32, "bold"),
            fg="white",
            bg="#1e1e1e"
        ).pack(pady=40)

        self.make_menu_button(frame, "Play Again", self.show_difficulty_menu)
        self.make_menu_button(frame, "Main Menu", self.show_main_menu)
        self.make_menu_button(frame, "Quit", self.window.destroy)

        self.switch_screen(frame)

    def make_menu_button(self, frame, text, command, small=False):
        tk.Button(
            frame,
            text=text,
            font=("Arial", 20 if not small else 14),
            width=12,
            command=command,
            bg="#3a3a3a",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            relief="flat",
            bd=0
        ).pack(pady=10)

    def run(self):
        self.window.mainloop()
