from mobs.hostile.HostileMob import HostileMob


class Skeleton(HostileMob):

    def __init__(self, health=25):
        super().__init__("Skeleton", health, "Common", "shot")
