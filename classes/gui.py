import customtkinter as ctk
import sys
from CTkMessagebox import CTkMessagebox

class GUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
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
            self.clear_content()
            print(f'{fName} vs {sName} | {rounds}')
        else:
            CTkMessagebox(title="Error", message="Wrong input data!!!", icon="cancel")

    def back_button_click(self) -> None:
        self.clear_content()
        self.create_menu()

    def exit_button_click(self) -> None:
        sys.exit(1)