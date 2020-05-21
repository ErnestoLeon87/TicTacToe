class Player:
    def __init__(self, mark=None, turn=False):
        self.name = None
        self.turn = False
        self._mark = mark
        self._move = 0

    def place_mark(self, move: int, field: list):
        if self.get_turn():  # Checking if it is player turn
            if len(field) < move:  # Check if it is a valid move
                raise Exception("This is not a valid move")
            else:
                if field[move-1] == " ":  # Check if that move have been done
                    field[move-1] = self._mark
                    self._move += 1
                    # self.set_turn(False)
                    return
                else:
                    raise Exception("Invalid move")
        else:
            raise Exception("It is not my turn yet")

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

    def get_num_move(self):
        return self._move

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name
