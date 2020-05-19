from game_lib.player import Player


class Game_Controller:
    def __init__(self, player_one: Player, player_two: Player):
        self.field = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self.player_one = player_one
        self.player_two = player_two

    def make_move(self, move: int):

        # Check if it is the player turn
        if self.player_one.get_turn():
            # Check if it is a valid move
            if len(self.field) < move:
                raise Exception("This is not a valid move")
            else:
                # Check if that move have been done
                if self.field[move-1] == " ":
                    self.field[move-1] = "X"
                    self.player_one.set_turn(False)
                    self.player_two.set_turn(True)
                    return
                else:
                    print("Invalid move")

        elif self.player_two.get_turn():
            # Check if it is a valid move
            if len(self.field) < move:
                raise Exception("This is not a valid move")
            else:
                # Check if that move have been done
                if self.field[move-1] == " ":
                    self.field[move-1] = "O"
                    self.player_one.set_turn(True)
                    self.player_two.set_turn(False)
                    return
                else:
                    print("Invalid move")

    def display_move(self):
        print("_________________")
        for i in range(0, len(self.field)):
            if i == 3 or i == 6:
                print("")
            print("|", self.field[i], "|", end=" ")
