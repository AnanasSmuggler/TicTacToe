import re
import sys


class Game:
    def __init__(self) -> None:
        self.__players = [{"name": "", "sign": "O", "points": 0}, {"name": "", "sign": "X", "points": 0}]
        self.__howManyToWin = 0

    # Method prepares the game setup. Currently the game is going in console. The future plans include GUI client, so this method is only a temporary placeholder
    def prepare_game(self, player1: str, player2: str, rounds: int) -> None:
        self.__set_player_one_name(player1)
        self.__set_player_two_name(player2)
        self.__set_how_many_to_win(rounds)

    def get_player_status(self, index: int) -> str:
        return f'[{self.__players[index]["sign"]}] {self.__players[index]["name"]} {self.__players[index]["points"]}' if index == 0 else f'{self.__players[index]["points"]} {self.__players[index]["name"]} [{self.__players[index]["sign"]}]'

    # Getter for current players move
    def get_player_on_move(self, emptySpaces: int) -> str:
        return self.__players[emptySpaces % 2]["sign"]
    
    # Setter for __playerOne
    def __set_player_one_name(self, name: str) -> None:
        self.__players[0]["name"] = name

    # Setter for __playerTwo
    def __set_player_two_name(self, name: str) -> None:
        self.__players[1]["name"] = name

    # Setter for __howManyToWin
    def __set_how_many_to_win(self, number: int) -> None:
        self.__howManyToWin = number

    # Adding one point to the winner of round
    def __add_points(self, index: int) -> None:
        self.__players[index]["points"] += 1

    # Adding half point for both players in case of a draw
    def __draw(self) -> None:
        self.__players[0]["points"] += 0.5
        self.__players[1]["points"] += 0.5
