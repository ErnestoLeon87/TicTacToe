from game_lib.game_controller import Game_Controller


if __name__ == "__main__":
    print("")
    print("")
    print("WELCOME")
    print(" TO ")
    print("TIC TAC TOE")
    print("")
    print("")
    print("Posible moves:")
    print("|1| |2| |3|")
    print("|4| |5| |6|")
    print("|7| |8| |9|")
    print("")

    controller = Game_Controller()
    controller.setup_game()
    controller.play()
