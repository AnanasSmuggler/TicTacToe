import classes.board

def main() -> None:
    print("Hello World!")
    board = classes.board.Board()
    board.insert_sign("X", 0, 0)
    board.show_board()
    board.insert_sign("O", 0, 0)
    board.insert_sign("O", 1, 1)
    board.insert_sign("X", 0, 1)
    board.show_board()
    

if __name__ == "__main__":
    main()
