class Player:

    name = None
    __health = 20

    def __init__(self, player_name):
        self.name = player_name

    def get_name(self):
        return self.name

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        self.__health = new_health

    def attacked(self, dmg):
        self.__health -= dmg
        return self.__health
