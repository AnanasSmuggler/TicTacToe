class Board:
    def __init__(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]

    #Resets board to default state
    def reset_board(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]
    
    #Inserts to board X or O - basic move in the game    
    def insert_sign(self, sign: str, row: int, column: int):
        self.__board[row][column] = sign

