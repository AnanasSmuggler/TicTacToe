class Board:
    def __init__(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]

    # Resets board to default state
    def reset_board(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]

    # Inserts to board X or O - basic move in the game
    def insert_sign(self, sign: str, row: int, column: int) -> None:
        if self.__board[row][column] == "": 
            self.__board[row][column] = sign

    #Prints board state in console
    def show_board(self) -> None:
        print(self.__board[0])
        print(self.__board[1])
        print(self.__board[2])