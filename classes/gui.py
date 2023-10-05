import customtkinter as ctk
import classes.game as g
import sys
import re
from CTkMessagebox import CTkMessagebox

class GUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.gameHandler = g.Game()
        self.create_menu()
        
    def create_menu(self) -> None:
        self.titleLabel = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.titleLabel.pack(pady=25)
        
        self.playButton = ctk.CTkButton(self.root, text="PLAY", command=self.play_button_click)
        self.playButton.pack(pady=25)

        self.exitButton = ctk.CTkButton(self.root, text="EXIT", command=self.exit_button_click)
        self.exitButton.pack(pady=25)
    
    def create_play_menu(self) -> None:
        self.titleLabel = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.titleLabel.pack(pady=25)
        
        self.labelNameF = ctk.CTkLabel(self.root, text="First Player:")
        self.labelNameF.pack()

        self.textInputNameF = ctk.CTkEntry(self.root)
        self.textInputNameF.pack(pady=10)
        
        self.labelNameS = ctk.CTkLabel(self.root, text="Second Player:")
        self.labelNameS.pack()

        self.textInputNameS = ctk.CTkEntry(self.root)
        self.textInputNameS.pack(pady=10)
        
        self.labelRounds = ctk.CTkLabel(self.root, text="How many rounds to win:")
        self.labelRounds.pack()

        self.textInputRounds = ctk.CTkEntry(self.root)
        self.textInputRounds.pack(pady=10)
        
        self.submitButton = ctk.CTkButton(self.root, text="START GAME", command=self.start_button_click)
        self.submitButton.pack(pady=5)
        
        self.backButton = ctk.CTkButton(self.root, text="GO BACK", command=self.back_button_click)
        self.backButton.pack(pady=5)
    
    def clear_content(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def play_button_click(self) -> None:
        self.clear_content()
        self.create_play_menu()

    def start_button_click(self) -> None:
        fName = self.textInputNameF.get()
        sName = self.textInputNameS.get()
        rounds = self.textInputRounds.get()
        if fName.strip() and sName.strip() and rounds.strip():
            if not re.match(r'^[1-9]\d*$', rounds):
                self.show_error("The rounds input is not a number!")
            else:
                self.clear_content()
                self.create_board()
        else:
            self.show_error("Empty inputs!")

    def create_board(self) -> None:
        self.frame = ctk.CTkFrame(master = self.root)
        self.frame.grid(row=0, column=0, ipadx=20, ipady=20, padx=20, pady=20, sticky="nsew")
        for i in range(3):
            for j in range(3):               
                self.board[i][j] = ctk.CTkButton(self.frame, text="", width=70, height=70, command=lambda row=i, col=j: self.make_move(row, col))
                self.board[i][j].grid(row=i, column = j)

    def make_move(self, row: int, col: int) -> None:
        self.board[row][col].configure(text="X", font=("Helvetica", 45))

    def back_button_click(self) -> None:
        self.clear_content()
        self.create_menu()

    def show_error(self, msg: str) -> None:
        CTkMessagebox(title="Error", message=msg, icon="cancel")

    def exit_button_click(self) -> None:
        sys.exit(1)