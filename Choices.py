from random import randint
from time import sleep


# Function made and used as a die to have randomization and okay percentage
def roll(times):
    rolled = randint(1, times)
    return rolled


# Function made to print to player the amount of health the enemy has
def life_left(entity):
    if entity.get_health() <= 0:
        print("The {} has 0 life left.\n".format(entity.get_name()))
    else:
        print("The {} has {} life left.\n".format(entity.get_name(), entity.get_health()))
    sleep(2)


# Function made to determine attack damage done to enemy mob
def atk_dmg(player, entity):
    dmg = roll(100)
    if dmg <= 20:
        print("The {} dodged your attack. Try again.".format(entity.get_name()))
    elif dmg <= 40:
        print("{} attacked the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 2))
        sleep(1)
        entity.attacked(2)
    elif dmg <= 60:
        print("{} attacked the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 3))
        sleep(1)
        entity.attacked(3)
    elif dmg <= 80:
        print("{} attacked the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 4))
        sleep(1)
        entity.attacked(4)
    elif dmg <= 100:
        print("{} attacked the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 5))
        sleep(1)
        entity.attacked(5)

    # Calls life left function
    life_left(entity)


# Function made to determine bow damage done to enemy mob
def bow_dmg(player, entity):
    dmg = roll(100)
    if dmg <= 17:
        print("You missed your shot, maybe next time {}!".format(player.get_name()))
        sleep(1)
    elif dmg <= 33:
        print("{} shot the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 7))
        sleep(1)
        entity.attacked(7)
    elif dmg <= 49:
        dmg = 8
        print("{} shot the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 8))
        sleep(1)
        entity.attacked(8)
    elif dmg <= 65:
        print("You missed your shot, maybe next time {}!".format(player.get_name()))
        sleep(1)
    elif dmg <= 82:
        print("{} shot the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 9))
        sleep(1)
        entity.attacked(9)
    elif dmg <= 100:
        print("{} shot the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 10))
        sleep(1)
        entity.attacked(10)

    # Calls life left function
    life_left(entity)


# Function made to determine potion damage done to enemy mob
def pot_dmg(player, entity):
    dmg = roll(100)
    if dmg <= 30:
        entity.attacked(12)
        print("{} threw a potion at the {} dealing {} damage.".format(player.get_name(), entity.get_name(), 12))
        sleep(1)
    else:
        print("Your potion did not hit the {}. Better luck next time.".format(entity.get_name()))

    # Calls life left function
    life_left(entity)


# Function made to determine damage done to player
def mob_dmg(player, entity):
    dmg = roll(100)
    if dmg <= 50:
        print("The {} missed it's attack. {} got lucky!".format(entity.get_name(), player.get_name()))
        sleep(1)
    # elif dmg == 3:
    #   print("The {} {} {}. They lost {} life.".format(entity.get_name(), entity.get_attack(), player.get_name(), dmg))
    #     sleep(1)
    #     player.attacked(dmg)
    elif dmg <= 68:
        dmg = 4
        print("The {} {} {}. They lost {} life.".format(entity.get_name(), entity.get_attack(), player.get_name(), dmg))
        sleep(1)
        player.attacked(dmg)
    elif dmg <= 82:
        dmg = 5
        print("The {} {} {}. They lost {} life.".format(entity.get_name(), entity.get_attack(), player.get_name(), dmg))
        sleep(1)
        player.attacked(dmg)
    elif dmg <= 100:
        dmg = 6
        print("The {} {} {}. They lost {} life.".format(entity.get_name(), entity.get_attack(), player.get_name(), dmg))
        sleep(1)
        player.attacked(dmg)

    # Prints to player their current health
    if player.get_health() <= 0:
        print("{} has 0 life left.\n".format(player.get_name()))
    else:
        print("{} has {} life left.\n".format(player.get_name(), player.get_health()))
    sleep(2)


# Function made for the player to pick how they want to attack the mob
# and soon to be how the mob attacks back
def picked(player, entity):

    wrong = 0

    # If both the player and the enemy is alive, then this while loop continues
    while entity.get_health() >= 1 and player.get_health() >= 1:

        # First asks for player input for the type of attack
        choice = input(
            'What would {} like to do?\n Type \'attack\' or \'a\' to attack\n Type \'shoot\' or '
            '\'s\' to shoot with your bow\n Type \'potion\' or \'p\' to throw a potion\n'
            '--> '.format(player.get_name()))
        choice.lower()

        """ For Future Use
        
        # If statement conditions of what mob type the player is facing
        if entity.get_name() == "Zombie":"""

        # Condition of what the players input is
        if choice in ("attack", "a"):
            atk_dmg(player, entity)
        elif choice in ("shoot", "s"):
            bow_dmg(player, entity)
        elif choice in ("potion", "p"):
            pot_dmg(player, entity)
        # elif choice == "e":
        #     entity.set_health(0)
        # elif choice == "d":
        #     player.set_health(0)
        else:
            print("That is not a possible action. Please choose a possible action.")
            sleep(1)
            wrong = 1

        # Determines mob damage
        if player.get_health() <= 0 or entity.get_health() <= 0 or wrong == 1:
            pass
        else:
            mob_dmg(player, entity)

        wrong = 0

        """ For Future Use
        
        elif entity.get_name() == "Skeleton":

            # Condition of what the players input is
            if choice in ("attack", "a"):
                atk_dmg(player, entity)
            elif choice in ("shoot", "s"):
                bow_dmg(player, entity)
            elif choice in ("potion", "p"):
                pot_dmg(player, entity)
            elif choice == "e":
                entity.set_health(0)
            elif choice == "d":
                player.set_health(0)

            # Determines mob damage
            if player.get_health() <= 0:
                pass
            else:
                mob_dmg(player, entity)

        elif entity.get_name() == "Spider":

            # Condition of what the players input is
            if choice in ("attack", "a"):
                atk_dmg(player, entity)
            elif choice in ("shoot", "s"):
                bow_dmg(player, entity)
            elif choice in ("potion", "p"):
                pot_dmg(player, entity)
            elif choice == "e":
                entity.set_health(0)
            elif choice == "d":
                player.set_health(0)

            # Determines mob damage
            if player.get_health() <= 0:
                pass
            else:
                mob_dmg(player, entity)"""

    if entity.get_health() <= 0:  # Executed if player kills the mob
        print("{} killed the {}".format(player.get_name(), entity.get_name()))
    elif player.get_health() <= 0:  # Executed if the player dies
        pass
