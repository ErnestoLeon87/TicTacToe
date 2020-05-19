class Player:
    def __init__(self, name, mark: str, turn=True):
        self.name = name
        self.turn = True
        self._mark = mark
        self.move = 0

    def make_move(self, move: int, field: list):

        if self.player_one.get_turn():  # Checking if it is player turn

            if len(self.field) < move:  # Check if it is a valid move
                raise Exception("This is not a valid move")
            else:

                if self.field[move-1] == " ":  # Check if that move have been done
                    self.field[move-1] = self.mark
                    self.set_turn(False)
                    return
                else:
                    print("Invalid move")

    def get_turn(self):
        return self.turn

    def set_turn(self, turn: bool):
        self.turn = turn

    def get_mark(self):
        return self._mark

    def set_mark(self, a_mark: str):
        if len(a_mark) > 1:
            raise Exception("This is not a valid mark.")
        else:
            self._mark = a_mark
