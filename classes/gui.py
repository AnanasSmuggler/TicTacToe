import customtkinter as ctk
import sys

class GUI:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x400")
        self.create_menu()
        
    def create_menu(self) -> None:
        self.title_label = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.title_label.pack(pady=25)
        
        self.name = ctk.CTkEntry(self.root, text="PLAY", command=self.play_button_click)
        self.playButton.pack(pady=25)

        self.exitButton = ctk.CTkButton(self.root, text="EXIT", command=self.exit_button_click)
        self.exitButton.pack(pady=25)
    
    def create_play_menu(self) -> None:
        self.title_label = ctk.CTkLabel(self.root, text="TIC TAC TOE", font=("Helvetica", 32))
        self.title_label.pack(pady=25)
        
        self.playButton = ctk.CTkButton(self.root, text="PLAY", command=self.play_button_click)
        self.playButton.pack(pady=25)

        self.exitButton = ctk.CTkButton(self.root, text="EXIT", command=self.exit_button_click)
        self.exitButton.pack(pady=25)
    
    def clear_content(self) -> None:
        for widget in self.root.winfo_children():
            widget.destroy()
        
    def play_button_click(self) -> None:
        self.clear_content()
        self.create_play_menu()

    def exit_button_click(self) -> None:
        sys.exit(1)