from .board import Board
import regex
import sys


class Game:
    def __init__(self) -> None:
        self.__playerOne = ""
        self.__playerTwo = ""
        self.__signs = ["O", "X"]
        self.__playerOnePoints = 0
        self.__playerTwoPoints = 0
        self.__howManyToWin = 0
        self.__board = Board()

    #Method prepares the game setup. Currently the game is going in console. The future plans include GUI client, so this method is only a temporary placeholder
    def prepare_game(self) -> None:
        self.__set_player_one_name(input("Welcome to Tic Tac Toe! Please enter first player name: \n"))
        self.__set_player_two_name(input("Please enter the second player name: \n"))
        while True:
            userInput = input("Enter the number of rounds needed to win [Press \'q\' to exit program]: \n")

            if userInput.lower() == 'q':
                sys.exit()
            else:
                if regex.match(r'^[1-9]\d*$', userInput):
                    self.__set_how_many_to_win(int(userInput))
                    break
                else:
                    print("Wrong entry! Please enter integer number that is higher than 0.\n")
        print(f'Let\'s start the game between {self.__playerOne} and {self.__playerTwo}! The first one to score {self.__howManyToWin} points wins!\n')

    #Setter for __playerOne
    def __set_player_one_name(self, name: str) -> None:
        self.__playerOne = name

    #Setter for __playerTwo
    def __set_player_two_name(self, name: str) -> None:
        self.__playerTwo = name

    #Setter for __howManyToWin
    def __set_how_many_to_win(self, number: int):
        self.__howManyToWin = number
