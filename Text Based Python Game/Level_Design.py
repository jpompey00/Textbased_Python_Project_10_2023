from Room import *


class LevelDesign:

    # The layout for all the rooms of the game
    room00 = Room(4, 2, [(4, 6), (3, 6)], ('', ''), ('', ''), (4, 5))

    room01 = Room(3, 2, [(1, 2), (1, 3)], (3, 5), (2, 5), (5, 4))
    room02 = Room(5, 2, [(3, 6), (4, 6)], (4, 5), (4, 4), (2, 2))
    room03 = Room(4, 2, [(6, 3), (6, 4)], (2, 4), (5, 3), (5, 5))
    room04 = Room(2, 3, [(4, 1), (5, 1)], (4, 3), (3, 2), (3, 5))
    room05 = Room(4, 5, [(1, 4), (1, 5)], (3, 2), (2, 4), (5, 2))
    room06 = Room(5, 4, [(5, 1), (4, 1)], (2, 5), (4, 2), (3, 2))
    room07 = Room(4, 5, [(6, 3), (6, 4)], (5, 3), (2, 5), (2, 2))
    boss_room08 = Room(2, 3, [('', ''), ('', '')], ('', ''), (5, 3), ('', ''))
    #boss_room08 = Room(2, 6, [(6, 3), (6, 4)], (5, 3), (2, 5), (2, 2))

    roomlist = [room00,room01,room02,room03,room04,room05,room06,room07,boss_room08]
