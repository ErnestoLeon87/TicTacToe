from game_lib.player import Player
from game_lib.field import Game_field


class Game_Controller:
    def __init__(self, field: Game_field, player_one: Player, player_two: Player):
        self.field = field
        self.player_one = player_one
        self.player_two = player_two

    def run_game(self):
        pass
