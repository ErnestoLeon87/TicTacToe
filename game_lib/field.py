class Field:
    def __init__(self):
        self.field = [" ", " ", " ",
                      " ", " ", " ",
                      " ", " ", " "]

    def show_moves(self):
        print("_________________")
        for i in range(0, len(self.field)):
            if i == 3 or i == 6:
                print("")
            print("|", self.field[i], "|", end=" ")
