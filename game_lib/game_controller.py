from game_lib.player import Player
from game_lib.field import Field


class Game_Controller:
    def __init__(self, name_one: str, one_mark: str, name_two: str, two_mark: str, field=Field):
        self.field = field
        self.player_one = Player(name_one)
        self.player_two = Player(name_two)
        self.player_one.set_mark(one_mark)
        self.player_two.set_mark(two_mark)

    def setup_game(self, first_move_name: str):
        if self.player_one.name == first_move_name:
            self.player_one.set_turn(True)
        elif self.player_two.name == first_move_name:
            self.player_two.set_turn(True)
        else:
            print("Please give a right name to start")

    def run_game(self):
        pass
