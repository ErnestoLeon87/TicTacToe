from game_lib.player import Player


class Game_Controller:
    player_one = None
    player_two = None

    def __init__(self, player_one: str, player_two: str):
        self.field = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)

    def make_move(self, move: int):

        player_one_turn = True
        player_two_turn = False
        # Check if it is the player turn
        if player_one_turn:
            # Check if it is a valid move
            if len(self.field) < move:
                raise Exception("This is not a valid move")
            else:
                # Check if that move have been done
                if self.field[move-1] == " ":
                    print("Valid Move")
                    self.field[move-1] = "X"
                    player_one_turn = False
                    player_two_turn = True
                    return
                else:
                    print("Invalid move")
        elif player_two_turn:
            # Check if it is a valid move
            if len(self.field) < move:
                raise Exception("This is not a valid move")
            else:
                # Check if that move have been done
                if self.field[move-1] == " ":
                    print("Valid Move")
                    self.field[move-1] = "O"
                    player_two_turn = False
                    player_one_turn = True
                    return
                else:
                    print("Invalid move")

    def display_move(self):
        for i in range(0, len(self.field)):
            if i == 3 or i == 6:
                print("")
            print("|", self.field[i], "|", end=" ")
