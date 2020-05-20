from game_lib.player import Player
from game_lib.field import Field


class Game_Controller:
    def __init__(self):
        self.field = Field()
        self.player_one = Player()
        self.player_two = Player()

    def setup_game(self):

        #  Setup player ONE name and mark
        one_name = input("Please enter first player name: ")
        self.player_one.set_name(one_name)
        self.__setup_mark(one_name)

        # Setup player TWO name and mark
        two_name = input("Please enter second player name: ")
        self.player_two.set_name(two_name)
        self.__setup_mark(two_name)

        # Setup who play first
        self.__setup_first_move()

    def __setup_mark(self, name):
        valid_mark = False
        while not valid_mark:
            one_mark = input(
                'Please give a mark for {}: '.format(name))
            try:
                if self.player_one.name == name:
                    self.player_one.set_mark(one_mark)
                    valid_mark = True
                if self.player_two.name == name:
                    self.player_two.set_mark(one_mark)
                    valid_mark = True
            except Exception as ex:
                print("Invalid mark.")

    def __setup_first_move(self):
        right_name = False
        while not right_name:
            first_move_name = input("First move name? ")
            if self.player_one.name == first_move_name:
                self.player_one.set_turn(True)
                right_name = True
            elif self.player_two.name == first_move_name:
                self.player_two.set_turn(True)
                right_name = True
            else:
                print("Please give a right name to start ",
                      self.player_one.name, " or ", self.player_two.name)

    def check_field_wins(self, parameter_list):
        pass

    def run_game(self):
        pass
