from Enemy import *
from Room import *
from Level_Design import *
import random
import matplotlib.pyplot as plt


# Main movement function
class Game:
    def __init__(self, player):
        self.room_list = LevelDesign.roomlist
        self.player = player
        self.load_room(self.room_list[0])
########################################################################################################################
    #Unneeded but will keep around
    walkable_area = {1: [2, 3, 4, 5], 2: [2, 3, 4, 5], 3: [2, 3, 4, 5], 4: [2, 3, 4, 5], 5: [2, 3, 4, 5],
                     6: [2, 3, 4, 5]}
########################################################################################################################
    # Here so I keep track of what variables I have.
    key_location = ''
    enemy_location = ''
    item_location = ''
    door_location = ''
    enemy = ''
    player_location_row = 2  # default spawn
    player_location_column = 3  # default spawn
    game_is_running = True
    prior_movement_stack = []
    level_count = 0
########################################################################################################################

    def set_enemy(self, enemy):
        self.enemy = enemy

    # When you make contact with an enemy, this function is called. Combat will occur, it subtracts the players attack
    # From the enemy HP and subtracts the enemy's attack from the player HP.
    # The player has a 100% hit chance while the enemy has a 70% hit chance
    # After running into an enemy to fight, the player will be moved back to their prior position using the movement
    # stack.
    def fight_enemy(self):
        # check for player hp after each turn.
        if (self.player_location_row, self.player_location_column) == self.enemy_location and self.enemy.isActive:
            random_atk = random.uniform(0,.25)
            if not self.player.has_dragon_spear:
                self.enemy.subtract_hp(self.player.atk + int(self.player.atk * random_atk))
                print(f"King Drake has taken {self.player.atk} damage" if self.enemy.isFinalEnemy else f"Enemy has taken {self.player.atk} damage")
            elif self.player.has_dragon_spear:
                self.enemy.subtract_hp(150)
                print(f"The Dragon Spear has done a big hit to King Drake! "
                      f"He has taken {150} Damage! The spear has broken! Finish King Drake")
                self.player.has_dragon_spear = False
        if self.enemy.hp <= 0:
            print(f"You have defeated King Drake!" if self.enemy.isFinalEnemy else f"Enemy defeated")
            self.enemy.isActive = False
            if self.enemy.isFinalEnemy and not self.enemy.isActive:
                self.you_win()
            self.pick_up_item()
            self.enemy_location = ('','') #deletes it's location for this room
        if self.enemy.isActive:  # retaliation damage
            random_number = random.randint(1,100)
            random_defense = random.uniform(0.07, 0.10)
            if random_number > 30:
                # This is the damage calculation which takes the enemy damage minus
                # a random percentage of the players defense stat
                enemy_atk_damage = self.enemy.dmg - int((self.enemy.dmg / (self.player.defence * random_defense)))
                self.player.subtract_hp(enemy_atk_damage)
                print(f'You took {enemy_atk_damage} damage')
                # checks if player HP is <=0
                self.is_game_over()
            else:
                print("They missed their attack.")
            self.player_location_row = self.prior_movement_stack[-1][0]
            self.player_location_column = self.prior_movement_stack[-1][1]
            self.prior_movement_stack.pop()
            print(self.enemy)




    # Function that controls the movement. Moves the character along the graph.
    # Takes input of 1-4 which corresponds to the direction they want to go. If there is a wall in the direction they
    # Want to go then they aren't able to move in that direction. If there is a door in that wall, it will check if the
    # Player has picked up the key and then load the next level if true. Logs all the movements to the
    # prior_movement_stack and if they haven't moved because of a wall, it will pop out that move.
    # Will print out their current location after moving
    def move_in_direction(self, direction):
        # if they move into a wall, i want it to say "you can't go that way and push them back out - maybe
        # noinspection PyTypeChecker

        self.prior_movement_stack.append((self.player_location_row, self.player_location_column))


        # For testing purposes ############################################################################
        # print(f'starting location [r,c]:({self.player_location_row},{self.player_location_column})')
        ###################################################################################################

        if (direction == 1) and (1 < self.player_location_row < 6):
            if self.player_location_row == 5:
                if (self.player_location_row + 1, self.player_location_column) in self.door_location:
                    self.go_through_door(self.room_list[self.level_count + 1])
                else:
                    print('You cannot go this way')
            else:
                self.player_location_row += 1
            print(f"Your location is (Row: {self.player_location_row}, Column: {self.player_location_column})")
        elif (direction == 2) and (1 < self.player_location_column < 6):
            if self.player_location_column == 5:
                if (self.player_location_row, self.player_location_column+1) in self.door_location:
                    self.go_through_door(self.room_list[self.level_count + 1])
                else:
                    print('You cannot go this way')
            else:
                self.player_location_column += 1
            print(f"Your location is (Row: {self.player_location_row}, Column: {self.player_location_column})")
        elif (direction == 3) and (1 < self.player_location_row < 6):
            if self.player_location_row == 2:
                if (self.player_location_row - 1, self.player_location_column) in self.door_location:
                    self.go_through_door(self.room_list[self.level_count + 1])
                else:
                    print('You cannot go this way')
            else:
                self.player_location_row -= 1
            print(f"Your location is (Row: {self.player_location_row}, Column: {self.player_location_column})")
        elif (direction == 4) and (1 < self.player_location_column < 6):
            if self.player_location_column == 2:
                if (self.player_location_row, self.player_location_column-1) in self.door_location:
                    self.go_through_door(self.room_list[self.level_count+1])
                else:
                    print('You cannot go this way')
            else:
                self.player_location_column -= 1
            print(f"Your location is (Row: {self.player_location_row}, Column: {self.player_location_column})")
        else:
            print('You cannot move any more in that direction')

            # For testing purposes ############################################################################
            print(f"ending location row: {self.player_location_row}, column: {self.player_location_column}")
            # For testing purposes ############################################################################

        # new function to check a list of things when stepped
        if not self.prior_movement_stack:
            print()
        else:
            if(self.player_location_row, self.player_location_column) == self.prior_movement_stack[-1]:
                self.prior_movement_stack.pop()
            else:
                self.check_over()


    # Function checks if the player has picked up the item for that room and what item they will recieve. The item for
    # the first rooms are decided by the players stats at the time. Depending on their health value, attack value,
    # max hp value etc.
    def pick_up_item(self):
        if ((self.player_location_row, self.player_location_column) == self.item_location and self.player.obtained_level_item == False)\
                or ((self.player_location_row, self.player_location_column) == self.enemy_location and self.enemy.isActive == False):
            if self.level_count == 7:
                print(f'You have found the Dragon Spear!')
                self.player.has_dragon_spear = True
            if self.player.hp < int(self.player.max_hp / 2):
                health_pot = int((self.player.max_hp - self.player.hp) / 2)
                print(f'You got a health potion!\nRegained {health_pot} health')
                self.player.add_hp(health_pot)
            elif self.player.hp > int(self.player.max_hp * .75) and self.player.atk < 65:
                print(f'You got a sword!\nGained 10 Attack!')
                self.player.add_atk(10)
            elif int(self.player.max_hp / 2) < self.player.hp < int(self.player.max_hp * .75):
                print(f'You got a helmet!\nMax HP Increased by 20')
                self.player.add_max_hp(20)
            elif int(self.player.max_hp * 9) < self.player.hp < int(self.player.max_hp):
                print(f'You got a Shield!\nDefence Increased by 5')
                self.player.add_def(5)
            else:
                print(f'You got a sword!\nGained 15 Attack!')
                self.player.add_atk(15)
            if (self.player_location_row, self.player_location_column) == self.item_location:
                self.item_location = ('', '')
                self.player.obtained_level_item = True

# Function is called to check players hp after a battle and determine if they have lost.
    def is_game_over(self):
        if self.player.hp <= 0:
            print("Game Over")
            self.game_is_running = False

# Function is called when you defeat king drake
    def you_win(self):
        print(f"You've defeated King Drake! You make your way out of the dungeon and and go to sell your spoils at the nearest Tavern!"
              f"\nThis adventuring thing may not be for you anymore!")
        self.game_is_running = False
        exit()

# Loads the room and places the items enemies, player and door based off the Room object.
# Resets all the checks needed for each room.
    def load_room(self, room):
        self.prior_movement_stack.clear()
        if self.level_count == 8:
            print("Loading boss room")
            self.player_location_row = room.player_location_row
            self.player_location_column = room.player_location_column
            #self.enemy.isFinalEnemy = True
            self.enemy = Enemy(self.player,True)
            self.enemy_location = room.enemy_location

        else:
            print(f"Loading level {self.level_count}" if self.level_count > 0 else "")
            self.player.obtained_level_item = False
            self.door_location = room.door_location
            self.item_location = room.item_location
            self.enemy_location = room.enemy_location
            self.player_location_row = room.player_location_row
            self.player_location_column = room.player_location_column
            self.enemy = Enemy(self.player)
            self.key_location = room.key_location
            self.player.has_key = False

# Function is called when the player makes contact with a door while having a key.
    def go_through_door(self, room):
        if self.player.has_key: #and ((self.player_location_row, self.player_location_column) in self.door_location)
            self.level_count += 1
            self.load_room(room)
        else:
            print("You have no key.")

# Level select for testing
    def level_select(self,room_number):
        self.level_count = room_number
        self.load_room(self.room_list[room_number])



# When the player makes contact with any point of interest on the map this function is called
# It checks for what exactly the player has made contact with and calls the appropriate function
    def check_over(self):  # TODO Cleanup!!!
        if (self.player_location_row, self.player_location_column) == self.key_location:
            self.player.has_key = True
            self.key_location = ('','')
            print('Picked up Key')
        elif (self.player_location_row, self.player_location_column) == self.enemy_location:
            print('Engaging Enemy')
            self.fight_enemy()

        elif (self.player_location_row, self.player_location_column) == self.item_location:
            print("Found Item")
            self.pick_up_item()
            self.item_location = ('','')
        elif len(self.prior_movement_stack) == 0:
            print('')
        else:
            print("Nothing Found!")

# This function uses pyplot to make a map of the room. Coloring the points of interest accordingly.
    def draw_map(self): #TODO make this drawn after every turn?
        plt.plot([1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], color='red')
        plt.plot([1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 1, 1], color='red')
        plt.plot([6, 6, 6, 6, 6, 6], [1, 2, 3, 4, 5, 6], color='red')
        plt.plot([1, 2, 3, 4, 5, 6], [6, 6, 6, 6, 6, 6], color='red')
        plt.plot(self.player_location_column, self.player_location_row, 'bo')
        if self.level_count == 8:

            plt.plot(self.enemy_location[1], self.enemy_location[0], 'ro', markersize=80)
        elif self.level_count == 0:
            plt.plot([(self.door_location[0][1]), self.door_location[1][1]],
                     [self.door_location[0][0], self.door_location[1][0]],
                     color='orange')
            if not self.player.has_key:
                plt.plot(self.key_location[1], self.key_location[0], 'yo')
        else:
            plt.plot([(self.door_location[0][1]), self.door_location[1][1]], [self.door_location[0][0], self.door_location[1][0]],
                     color='orange')  # change this color maybe
            if self.enemy.isActive:
                plt.plot(self.enemy_location[1], self.enemy_location[0], 'ro')
            if not self.player.has_key:
                plt.plot(self.key_location[1], self.key_location[0], 'yo')
            if not self.player.obtained_level_item:
                plt.plot(self.item_location[1], self.item_location[0], 'go')
        plt.show()

# Function returns all the points of interest in a string. For testing purposes
    def __str__(self):
        return f"{self.door_location}, {self.item_location}, {self.enemy_location}, {self.player_location_row}, {self.player_location_column}"
