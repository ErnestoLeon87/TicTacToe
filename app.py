from game_lib.game_controller import Game_Controller, Player


if __name__ == "__main__":
    player_one_name = "Rebeca"
    player_two_name = "Ernesto"
    player_one = Player(player_one_name, "X")
    player_two = Player(player_two_name, "O")

    game = Game_Controller(player_one, player_two)

    player_one.make_move(1, game.field)

    player_two.make_move(2, game.field)

    game.display_move()

    print("")
