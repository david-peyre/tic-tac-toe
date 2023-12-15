import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Initialisation de la fenêtre Tkinter
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Initialisation du joueur actuel et du tableau de jeu
        self.current_player = "X"
        self.board = [""] * 9

        # Création des boutons pour le tableau de jeu
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Helvetica", 24), width=10, height=5,
                                   command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)

    def make_move(self, row, col):
        # Fonction appelée lorsqu'un joueur fait un mouvement
        index = row * 3 + col
        if self.board[index] == "":
            # Vérifie si la case est vide avant de faire un mouvement
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                # Vérifie s'il y a un gagnant
                self.show_winner()
                self.reset_game()
            elif "" not in self.board:
                # Vérifie s'il y a un match nul (pas de gagnant et plus de cases vides)
                self.show_draw()
                self.reset_game()
            else:
                # Passe au joueur suivant s'il n'y a pas de gagnant ni de match nul
                self.switch_player()

    def update_button(self, row, col):
        # Met à jour le texte du bouton après un mouvement
        index = row * 3 + col
        button = self.window.grid_slaves(row=row, column=col)[0]
        button.config(text=self.current_player, state=tk.DISABLED)

    def switch_player(self):
        # Passe au joueur suivant
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Vérifie s'il y a un gagnant
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
        # Affiche la boîte de dialogue pour indiquer le gagnant
        messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")

    def show_draw(self):
        # Affiche la boîte de dialogue pour indiquer un match nul
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")

    def reset_game(self):
        # Réinitialise le jeu pour une nouvelle partie
        self.current_player = "X"
        self.board = [""] * 9
        for button in self.window.grid_slaves():
            button.config(text="", state=tk.NORMAL)

    def run(self):
        # Lance la boucle principale de la fenêtre Tkinter
        self.window.mainloop()

# Exécute le jeu si le fichier est exécuté directement
if __name__ == "__main__":
    game = TicTacToe()
    game.run()
