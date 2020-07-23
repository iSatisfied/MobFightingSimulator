from mobs.Mob import Mob


class HostileMob(Mob):

    def __init__(self, mob_name, mob_health, mob_rarity, mob_attack):
        super().__init__("Hostile", mob_name, mob_health, mob_rarity)
        self.attack = mob_attack
    
    def attacked(self, damage):
        self.health -= damage
        return self.health

    def get_attack(self):
        return self.attack