class Mob:

    def __init__(self, mob_type, mob_name, mob_health, mob_rarity):
        self.entity_type = mob_type
        self.name = mob_name
        self.health = mob_health
        self.rarity = mob_rarity

    def get_entity_type(self):
        return self.entity_type
    
    def get_name(self):
        return self.name

    def get_rarity(self):
        return self.rarity

    def get_health(self):
        return self.health

    def set_health(self, new_health):
        self.health = new_health
