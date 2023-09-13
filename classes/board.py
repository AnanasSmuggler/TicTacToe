class Board:
    def __init__(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.__emptySpaces = 9

    # Resets board to default state
    def reset_board(self) -> None:
        self.__board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.__emptySpaces = 9

    # Inserts to board X or O - basic move in the game
    def insert_sign(self, sign: str, row: int, column: int) -> None:
        if self.__board[row][column] == "":
            self.__board[row][column] = sign
            self.__emptySpaces -= 1

        if self.__emptySpaces <= 4:
            if self.check_win(sign):
                print(f'Gratulacje! Grę zwycięża {sign}!')

    #Prints board state in console
    def show_board(self) -> None:
        print(self.__board[0])
        print(self.__board[1])
        print(self.__board[2])

    #Checks if the given sign has won
    def check_win(self, sign: str) -> bool:
        return self.__check_row(sign) or self.__check_column(sign) or self.__check_diagonal(sign)

    #Private helper for check_win - checks every row
    def __check_row(self, sign: str) -> bool:
        winning_row = [sign, sign, sign]
        return self.__board[0] == winning_row or self.__board[1] == winning_row or self.__board[2] == winning_row

    #Private helper for check_win - checks every column
    def __check_column(self, sign: str) -> bool:
        for col in range(3):
            if self.__board[0][col] == self.__board[1][col] == self.__board[2][col] == sign:
                return True
        return False

    #Private helper for check_win - checks every diagonal
    def __check_diagonal(self, sign: str) -> bool:
        return self.__board[0][0] == self.__board[1][1] == self.__board[2][2] == sign or self.__board[0][2] == self.__board[1][1] == self.__board[2][0] == sign
