from mobs.hostile.HostileMob import HostileMob


class Spider(HostileMob):

    def __init__(self, health=50):
        super().__init__("Spider", health, "Common", "bit")
