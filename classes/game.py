import re
import sys


class Game:
    def __init__(self) -> None:
        self.__players = [{"name": "", "sign": "O", "points": 0}, {"name": "", "sign": "X", "points": 0}]
        self.__howManyToWin = 0

    # Method prepares the game setup. Currently the game is going in console. The future plans include GUI client, so this method is only a temporary placeholder
    def prepare_game(self, player1: str, player2: str, rounds: int) -> None:
        self.__reset_players()
        self.__set_player_one_name(player1)
        self.__set_player_two_name(player2)
        self.__set_how_many_to_win(rounds)

    # Resets state of players
    def __reset_players(self) -> None:
        self.__players = [{"name": "", "sign": "O", "points": 0}, {"name": "", "sign": "X", "points": 0}]

    # Returns string with the names, signs and points of players used in gui board
    def get_player_status(self, index: int) -> str:
        return f'[{self.__players[index]["sign"]}] {self.__players[index]["name"]} {self.__players[index]["points"]}' if index == 0 else f'{self.__players[index]["points"]} {self.__players[index]["name"]} [{self.__players[index]["sign"]}]'

    # Getter for current players move
    def get_player_on_move(self, emptySpaces: int) -> str:
        return self.__players[emptySpaces % 2]["sign"]
    
    def get_player_name_by_sign(self, sign: str) -> str:
        for player in self.__players:
            if player["sign"] == sign:
                return player["name"]
        return ""
    
    # Setter for __playerOne
    def __set_player_one_name(self, name: str) -> None:
        self.__players[0]["name"] = name

    # Setter for __playerTwo
    def __set_player_two_name(self, name: str) -> None:
        self.__players[1]["name"] = name

    # Setter for __howManyToWin
    def __set_how_many_to_win(self, number: int) -> None:
        self.__howManyToWin = number

    # Method adds point for player that won round
    def round_won(self, sign: str) -> bool:
        for player in self.__players:
            if player["sign"] == sign:
                player["points"] +=1
        self.__switch_players()
                
    # Method adds half point for both players in case of a draw
    def draw(self) -> None:
        self.__players[0]["points"] += 0.5
        self.__players[1]["points"] += 0.5
        self.__switch_players()

    # Method switches players dict in lists. The purpose of this method is to switch player that will start the round
    def __switch_players(self) -> None:
        self.__players[0], self.__players[1] = self.__players[1], self.__players[0]
        
    # Method that checks if someone won the game 
    def is_game_over(self) -> bool:
        return self.__players[0]["points"] >= self.__howManyToWin or self.__players[1]["points"] >= self.__howManyToWin
    