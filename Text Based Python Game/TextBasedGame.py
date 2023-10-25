from CLI import CLI
from Game import *
from Player import *

# Julian Pompey


if __name__ == '__main__':
    name = input("Please enter your name... \n")
    #name = 'TestName'
    player = Player(name)
    game = Game(player)
    cli = CLI(game)

# TODO uncomment
    cli.start()
    cli.explanation()

    while game.game_is_running:
        cli.main_menu()


