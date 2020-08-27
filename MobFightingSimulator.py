# A Minecraft mob fighting simulator
# Possibly for WMCAT but mainly for fun
# By: Francisco Magana

from Player import Player
from Choices import picked, roll, fight
from mobs.hostile.Skeleton import Skeleton
from mobs.hostile.Spider import Spider
from mobs.hostile.Zombie import Zombie
from time import sleep


# Initializes variables to start game and determine room number
game = True
room_number = 1
name = ""
character = ""


class MobFightingSimulator:

    # Code only executes in this class when this is the main file
    if __name__ == "__main__":
        print("Welcome to a mob fighting simulator!")  # Introduction to the game
        sleep(1)
        name = input("What would you like your player's name to be?\n--> ")  # Asks for players name
        character = Player(name)  # Creates player object with players name

        while game:  # While the game variable is true, code executes
            print("Well {}, just enter into the first door to continue.\n".format(name)) # Intro to the game mechanics
            
            if not fight(character, Zombie(), False):
                game = False
                break

            print("Well done {}! You have completed room one, now time for room two.".format(character.get_name()))
            room_number += 1
            character.set_health(20)
            print("But first, here is a heal.\n")

            if not fight(character, Skeleton(), False):
                game = False
                break

            print("Good job {}! You have completed room two, now time for room three.".format(character.get_name()))
            room_number += 1
            character.set_health(20)
            print("Here comes another heal!\n")

            if not fight(character, Spider(), True):
                game = False
                break


        if character.get_health() <= 0:  # Executes if player dies
            print("You have died {}. Thanks for playing!!".format(character.get_name()))
            print("You made it to room {}.".format(room_number))
        else:  # Executes if player completes the game
            print("Congratulations {}! You have completed the mob fighting simulator!".format(character.get_name()))

