class Player:
    def __init__(self,name):
        self.name = name

    # Starting stats for the player.
    max_hp = 100
    base_max_hp = 100
    hp = 100
    defence = 25
    atk = 10
    base_atk = 10
    has_key = False
    has_dragon_spear = False

    # TODO make dragon spear stat visible to player or have attack increase by insane amount.
    # Not visible to player.
    obtained_level_item = False

    # Different functions that edit the players stats
    def subtract_hp(self,damage):
        self.hp -= damage

    def add_hp(self, heal):
        self.hp += heal

    def add_max_hp(self, increase):
        self.max_hp += increase

    def add_def(self, increase):
        self.defence += increase

    def add_atk(self,increase):
        self.atk+=increase

# A write-up of the stats for the player.
    def __str__(self):
        return (f'Name: {self.name} \nHp: {self.hp} / {self.max_hp} \nDefense: {self.defence} \nAttack: {self.atk}'
                f'\nHas a key? {"Yes" if self.has_key else "No"}'
                f'\n{"Has the Dragon Spear!" if self.has_dragon_spear else""}')
