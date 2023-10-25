class Enemy:
    hp = ''
    max_hp = ''
    dmg = ''
    isActive = ''
    isFinalEnemy = ''

 # Each enemy has their hp and damage that they do pulled from the players stats at the time
    def __init__(self, player, final_enemy=False):
        self.isFinalEnemy = final_enemy
        if self.isFinalEnemy == False:
            self.hp = int(player.max_hp - (player.base_max_hp * 0.45))
            #self.hp = 1 testing variable
            self.dmg = int(player.base_atk + (player.base_max_hp * 0.13))
            self.isActive = True
        else:
            self.hp = int((player.max_hp * .6 )+ 150)
            self.max_hp = self.hp
            #self.hp = int(151)
            # (current hp - max hp ) * -.15
            self.dmg = int(player.base_atk + (player.base_max_hp * 0.13))
            self.isActive = True




# Functions to control the stats of the enemy
    def subtract_hp(self, damage):
        self.hp -= damage
        # if the final enemy is king drake, his attack rises as his HP falls.
        if self.isFinalEnemy:
            self.dmg = self.dmg + ((self.hp - self.max_hp) * -.15)

    def set_active(self): #may not need
        self.isActive = not self.isActive

    def __str__(self):
        return f"\nKing Drake\nHP: {self.hp}, ATTACK: {self.dmg}" if self.isFinalEnemy else f"\nEnemy\nHP: {self.hp}, ATTACK: {self.dmg}"
