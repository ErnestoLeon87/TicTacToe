from game_lib.game_controller import Game_Controller


if __name__ == "__main__":
    player_one_name = "Rebeca"
    player_two_name = "Ernesto"
    game = Game_Controller(player_one_name, player_two_name)

    game.make_move(5)
    game.display_move()
    print("")
    game.make_move(1)
    game.display_move()
    print("")
    game.make_move(9)
    game.display_move()
    print("")
    game.display_move()
