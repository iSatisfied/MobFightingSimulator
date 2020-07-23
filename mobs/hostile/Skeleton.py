from mobs.hostile.HostileMob import HostileMob


class Skeleton(HostileMob):

    def __init__(self, health=20):
        super().__init__("Skeleton", health, "Common", "shot")
