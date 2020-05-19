from game_lib.game_controller import Game_Controller, Player


if __name__ == "__main__":
    player_one_name = "Rebeca"
    player_two_name = "Ernesto"
    player_one = Player(player_one_name)
    player_two = Player(player_two_name)

    game = Game_Controller(player_one, player_two)

    game.make_move(5)
    game.display_move()
    print("")
    game.make_move(1)
    game.display_move()
    print("")
    game.make_move(9)
    game.make_move(4)
    game.make_move(3)
    game.make_move(6)
    game.make_move(7)

    game.display_move()
    print("")
