from .board import Board
import re
import sys


class Game:
    def __init__(self) -> None:
        self.__players = [{"name": "", "sign": "O", "points": 0}, {"name": "", "sign": "X", "points": 0}]
        self.__howManyToWin = 0
        self.__board = Board()

    # Method prepares the game setup. Currently the game is going in console. The future plans include GUI client, so this method is only a temporary placeholder
    def prepare_game(self, player1: str, player2: str, rounds: int) -> None:
        self.__set_player_one_name(input("Welcome to Tic Tac Toe! Please enter first player name: \n"))
        self.__set_player_two_name(input("Please enter the second player name: \n"))
        while True:
            userInput = input("Enter the number of rounds needed to win [Press \'q\' to exit program]: \n")

            if userInput.lower() == 'q':
                sys.exit()
            else:
                if re.match(r'^[1-9]\d*$', userInput):
                    self.__set_how_many_to_win(int(userInput))
                    break
                else:
                    print("Wrong entry! Please enter integer number that is higher than 0.\n")
        print(f'Let\'s start the game between {self.__players[0]["name"]} and {self.__players[1]["name"]}! The first one to score {self.__howManyToWin} points wins!\n')
        while True:
            inp = input("Are you ready? [y/n]: \n")
            if inp.lower() == 'y':
                self.__gameplay()
            break

    # Handles whole gameplay
    def __gameplay(self) -> None:
        while True:
            if self.__players[0]["points"] >= self.__howManyToWin or self.__players[1]["points"] >= self.__howManyToWin:
                print(f'End of the match! The score is: {self.__players[0]["name"]} {self.__players[0]["points"]} - {self.__players[1]["name"]} {self.__players[1]["points"]}')
                break
            else:
                print(f'The score is: {self.__players[0]["name"]} {self.__players[0]["points"]} - {self.__players[1]["name"]} {self.__players[1]["points"]}')
                self.__start_game()
                self.__players[0], self.__players[1] = self.__players[1], self.__players[0]

    # Starts the single round of Tic Tac Toe
    def __start_game(self) -> None:
        i = 0
        self.__board.show_board()
        while i < 9:
            move = input(f'{self.__players[i % 2]["name"]}, what\'s your next move?\n')
            if re.match(r'^[012]{2}$', move) and self.__board.insert_sign(self.__players[i % 2]["sign"], int(move[0]), int(move[1])):
                self.__board.show_board()
                if self.__board.check_win(self.__players[i % 2]["sign"]):
                    print(f'{self.__players[i % 2]["name"]} has won this round!')
                    self.__add_points(i % 2)
                    break
                i += 1
            else:
                print("Wrong move! Try again!")
        if i == 9:
            print("Draw!")
            self.__draw()
        self.__board.reset_board()

    # Adding one point to the winner of round
    def __add_points(self, index: int) -> None:
        self.__players[index]["points"] += 1

    # Adding half point for both players in case of a draw
    def __draw(self) -> None:
        self.__players[0]["points"] += 0.5
        self.__players[1]["points"] += 0.5
