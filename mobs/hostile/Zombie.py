from mobs.hostile.HostileMob import HostileMob


class Zombie(HostileMob):

    def __init__(self, health=20):
        super().__init__("Zombie", health, "Common", "strucked")

