import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [""] * 9

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 24), width=10, height=5,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                self.show_winner()
                self.reset_game()
            elif "" not in self.board:
                self.show_draw()
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        index = row * 3 + col
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        for i in range(3):
            if self.board[i*3] == self.board[i*3+1] == self.board[i*3+2] != "":
                return True
            if self.board[i] == self.board[i+3] == self.board[i+6] != "":
                return True

        if self.board[0] == self.board[4] == self.board[8] != "":
            return True 
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True 

        return False

    def show_winner(self):
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")

    def show_draw(self):
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.window.grid_slaves():
            button.config(text="", state=tk.NORMAL)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
