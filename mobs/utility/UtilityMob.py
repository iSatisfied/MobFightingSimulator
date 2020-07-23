from mobs.Mob import Mob

class UtilityMob(Mob):

    def __init__(self, mob_name, mob_health, mob_rarity):
        super().__init__("Utility", mob_name, mob_health, mob_rarity)
