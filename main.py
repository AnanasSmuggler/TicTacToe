import classes.gui as gui
import customtkinter as ctk


def main() -> None:
    root = ctk.CTk()
    gui.GUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
