import classes.game as g
import classes.gui as gui
import customtkinter as ctk


def main() -> None:
    #game = g.Game()
    #game.prepare_game()
    root = ctk.CTk()
    my_window = gui.GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
