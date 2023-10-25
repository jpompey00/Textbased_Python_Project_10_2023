import matplotlib.pyplot as plt
class Room:

    # The interface for the room objects in Level_Design.py.

    def __init__(self, player_location_row, player_location_column, door_location,item_location,enemy_location, key_location):
        self.door_location = door_location
        self.item_location = item_location
        self.enemy_location = enemy_location
        self.player_location_column = player_location_column
        self.player_location_row = player_location_row
        self.key_location = key_location




