from mobs.Mob import Mob


class BossMob(Mob):

    def __init__(self, mob_name, mob_health, mob_rarity):
        super().__init__("Boss", mob_name, mob_health, mob_rarity)

