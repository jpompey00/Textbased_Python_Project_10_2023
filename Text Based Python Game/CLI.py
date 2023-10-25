
class CLI:
    def __init__(self, game):
        self.game = game

    def start(self):
        print('While exploring a ruin you accidentally fell into the deep dungeon.\nYou must make your way out'
               'of the deep dungeon by finding keys and beating the guardian of the dungeon, King Drake.'
               '\nBefore your fell you picked up a map that has the ability to update based on your surroundings.'
              '\nFind keys and find your way out of the dungeon.\n')
        input('Press Enter to Continue...\n')

    def explanation(self):
        print('Move throughout the dungeon and interact with items on the map by stepping on them.'
              '\nRed Mark - Enemy\nBlue Mark - Item\nYellow Mark - Key\nDoors are marked by Orange Lines'
              '\nBattle with enemies will begin on contact. You attack first then the enemy retaliates.'
              '\nItems will change based on your stats and what you need.'
              '\nDefeated enemies will drop items for you as well'
              '\nFind your way out without perishing. Weigh the risks and rewards of fighting enemies and not\n')
        input('Press Enter to Continue...\n')


# This handles the choices that you see from the main menu. Once selected it passes the functions located in the game
# Object
    def main_menu(self):
        print('1 - Move \n2 - Check Stats\n3 - Check Map')
        choice = int(input('Chose an option... '))

        if choice == 1:
            print('Choose a direction\n1 - North\n 2 - East\n3 - South\n 4 - West')
            direction = int(input())
            self.game.move_in_direction(direction)
        elif choice == 2:
            print(self.game.player)

        elif choice == 3:
            self.game.draw_map()

        # level select for testing purposes
        elif choice == 8:
            level = int(input("\n0\n1\n2\n3\n4\n5\n6\n7\n8"))
            self.game.level_select(level)



