import customtkinter as ctk
import classes.game as g
import classes.board as b
import sys
import re
from CTkMessagebox import CTkMessagebox

class GUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("450x550")
        self.buttons = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.gameHandler = g.Game()
        self.gameBoard = b.Board()
        self.create_menu()
        
    # The first menu that appears in the window. It has two buttons: "PLAY" and "EXIT"
    def create_menu(self) -> None:
        self.titleLabel = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.titleLabel.pack(pady=25)
        
        self.playButton = ctk.CTkButton(self.root, text="PLAY", command=self.play_button_click)
        self.playButton.pack(pady=25)

        self.exitButton = ctk.CTkButton(self.root, text="EXIT", command=self.exit_button_click)
        self.exitButton.pack(pady=25)
    
    # The menu that appears after clicking "PLAY" button in first menu. It includes form that will allow to start the game
    def create_play_menu(self) -> None:
        self.titleLabel = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.titleLabel.pack(pady=25)
        
        self.labelNameF = ctk.CTkLabel(self.root, text="First Player:")
        self.labelNameF.pack()

        self.textInputNameF = ctk.CTkEntry(self.root)
        self.textInputNameF.pack()
        
        self.labelNameS = ctk.CTkLabel(self.root, text="Second Player:")
        self.labelNameS.pack()

        self.textInputNameS = ctk.CTkEntry(self.root)
        self.textInputNameS.pack()
        
        self.labelRounds = ctk.CTkLabel(self.root, text="How many rounds to win:")
        self.labelRounds.pack()

        self.textInputRounds = ctk.CTkEntry(self.root)
        self.textInputRounds.pack()
        
        self.submitButton = ctk.CTkButton(self.root, text="START GAME", command=self.start_button_click)
        self.submitButton.pack(pady=15)
        
        self.backButton = ctk.CTkButton(self.root, text="GO BACK", command=self.back_button_click)
        self.backButton.pack(pady=15)
    
    # This method clears all content inside the current window
    def clear_content(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # The event that happens on clicking "PLAY" button in first menu. Clears the window and creates play menu form    
    def play_button_click(self) -> None:
        self.clear_content()
        self.create_play_menu()

    # This button collects the form data and verifies it. Then it clears the window and creates the gameboard
    def start_button_click(self) -> None:
        fName = self.textInputNameF.get()
        sName = self.textInputNameS.get()
        rounds = self.textInputRounds.get()
        if fName.strip() and sName.strip() and rounds.strip():
            if not re.match(r'^[1-9]\d*$', rounds):
                self.show_error("The rounds input is not a number!")
            else:
                self.gameHandler.prepare_game(fName, sName, int(rounds))
                self.clear_content()
                self.create_board()
                self.show_checkmark(f'The first player to score {rounds} points wins the game. Good luck!', "Start game")
        else:
            self.show_error("Empty inputs!")

    # Method creates gameboard with 3x3 grid of buttons that will handle all gameplay
    def create_board(self) -> None:
        self.gameBoard.reset_board()
        
        self.scoreFrame = ctk.CTkFrame(master = self.root,  width=430, height=40)
        self.scoreFrame.grid(row=0, column=0, sticky="ew", pady=15)
        self.scoreFrame.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
        
        self.scoreLabel = ctk.CTkLabel(self.scoreFrame, text=f'{self.gameHandler.get_player_status(0)} - {self.gameHandler.get_player_status(1)}', font=("Helvetica", 32))
        self.scoreLabel.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        self.boardFrame = ctk.CTkFrame(master = self.root)
        self.boardFrame.grid(row=1, column=0, sticky="ew", pady=15)
        self.boardFrame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        for i in range(3):
            for j in range(3):               
                self.buttons[i][j] = ctk.CTkButton(self.boardFrame, text="", width=80, height=80, command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column = j, padx=(15,15), pady=(15,15))

        self.root.grid_columnconfigure(0, weight=1)
        
    # Event after button on gameboard is clicked - a simple move in the game
    def make_move(self, row: int, col: int) -> None:
        sign = self.gameHandler.get_player_on_move(self.gameBoard.getEmptySpaces())
        if self.gameBoard.insert_sign(sign, row, col):
            self.buttons[row][col].configure(text=sign, font=("Helvetica", 45))
            if self.gameBoard.getEmptySpaces() < 5:
                if  self.gameBoard.check_win(sign):
                    if self.gameHandler.round_won(sign):
                        self.clear_content()
                        self.create_menu()
                        self.show_checkmark(f'Game Over! The score is:\n {self.gameHandler.get_player_status(0)} - {self.gameHandler.get_player_status(1)}', "GG")
                    else:
                        self.clear_content()
                        self.create_board()
                        self.show_checkmark(f'The winner of this round is {self.gameHandler.get_player_name_by_sign(sign)}!', "Go Next")
                else:
                    if self.gameBoard.getEmptySpaces() == 0:
                        self.gameHandler.draw()
                        self.reset_gui_board()
                        self.show_checkmark(f'Draw!', "Go Next")
    
    # Resets the game board
    def reset_gui_board(self) -> None:
        self.clear_content()
        self.create_board()
    
    # Event that happens after clicking "GO BACK" button in the play menu. Clears the window and creates first menu
    def back_button_click(self) -> None:
        self.clear_content()
        self.create_menu()

    # Method pop up an error window
    def show_error(self, msg: str) -> None:
        CTkMessagebox(title="Error", message=msg, icon="cancel")
        
        # Method pop up an error window
    def show_checkmark(self, msg: str, opt1: str) -> None:
        CTkMessagebox(title="Tic Tac Toe", message=msg, icon="check", option_1=opt1)

    # Event after clicking "EXIT" button. Shuts down whole application
    def exit_button_click(self) -> None:
        sys.exit(1)