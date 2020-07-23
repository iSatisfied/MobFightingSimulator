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

    


    """

        UTILITY MOBS
    _______________________
        Villager
        Wolf
        Horse
        Ocelot
        Pigmen
        Zombie/Skeleton Horse

        HOSTILE MOBS
    _______________________
        Enderman
        Zombie Pigman
        Polar Bear
        Cave Spider
        Blaze
        Creeper
        Ghast
        Magma cube
        Silverfish
        Slime
        Spider Jockey
        Zombie Villager
        Wither Skeleton
        Witch
        Evoker
        Vindicator
        Vex
        Chicken Jockey
        Endermite
        Guardian
        Killer Bunny
        Baby Zombie
        Shulker
        Zombie/Skeleton Horseman
        Husk
        Stray
        Phantom

        BOSSES / MINI-BOSSES
    __________________________
        Giant
        Elder Guardian
        Master Phantom
        Wither
        Ender Dragon
        Illusioner
        Red Dragon

    """
