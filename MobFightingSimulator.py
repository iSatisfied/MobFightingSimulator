# A Minecraft mob fighting simulator
# Possibly for WMCAT but mainly for fun
# By: Francisco Magana

from Player import Player
from Choices import picked, roll
from mobs.hostile.Skeleton import Skeleton
from mobs.hostile.Spider import Spider
from mobs.hostile.Zombie import Zombie
from time import sleep

"""
Easy TODO:
- Add more mob types
- Differentiate mob accuracies
- Add more mob attacks
- Add final boss
- Add mini bosses
- Add drops
- Add armor
- Add uses

Iffy TODO:
- Add inventory
- Improve accuracy choices
- Other worlds

Complex TODO:
- Add machine learning
- Add AI
- Add deep learning
"""

# Initializes variables to start game and determine room number
ingame = True
room_number = 1


class MobFightingSimulator:

    # Code only executes in this class when this is the main file
    if __name__ == "__main__":
        print("Welcome to a mob fighting simulator!")  # Introduction to the game
        sleep(1)
        name = input("What would you like your player's name to be?\n--> ")  # Asks for players name
        character = Player(name)  # Creates player object with players name

        while ingame:  # While the game variable is true, code executes
            print("Well {}, just enter into the first door to continue.\n".format(name)) # Intro to the game mechanics
            sleep(2)
            mobs = roll(2)  # rolls for different types of the same mob

            # Determines when what type of Zombie mob
            # Current differences are just health
            if mobs == 1:
                entity = Zombie()
            else:
                entity = Zombie(health=15)

            print("{} has encountered a {} with {} health.".format(character.get_name(), entity.get_name(), entity.get_health()))  # Prints the encounter
            picked(character, entity)  # Executes picked function for the fighting simulation

            # Determines if the player dies, then changes the game variable to false to leave game loop
            if character.get_health() <= 0:
                game = False
                break

            # Prompts player to next room and increases room_number variable
            print("Well done {}! You have completed room one, now time for room two.".format(character.get_name()))
            room_number += 1
            character.set_health(20)
            print("But first, here is a heal.\n")
            sleep(1)
            mobs = roll(2)  # rolls for different types of the same mob

            # Determines when what type of Skeleton mob
            # Current differences are just health
            if mobs == 1:
                entity = Skeleton()
            else:
                entity = Skeleton(health=25)

            print("{} has encountered a {} with {} health.".format(character.get_name(), entity.get_name(), entity.get_health()))  # Prints the encounter
            picked(character, entity)  # Executes picked function for the fighting simulation

            # Determines if the player dies, then changes the game variable to false to leave game loop
            if character.get_health() <= 0:
                game = False
                break

            # Prompts player to next room and increases room_number variable
            print("Good job {}! You have completed room two, now time for room three.".format(character.get_name()))
            room_number += 1
            character.set_health(20)
            print("Here comes another heal!\n")
            sleep(1)
            mobs = roll(2)  # rolls for different types of the same mob

            # Determines when what type of Spider mob
            # Current differences are just health
            if mobs == 1:
                entity = Spider()
            else:
                entity = Spider(health=40)

            print("{} has encountered a {} with {} health.".format(character.get_name(), entity.get_name(), entity.get_health()))  # Prints the encounter
            picked(character, entity)  # Executes picked function for the fighting simulation

            # Determines if the player dies, then changes the game variable to false to leave game loop
            if character.get_health() <= 0:
                game = False
                break

            # Player has completed the simulator and exits game loop
            game = False

        if character.get_health() <= 0:  # Executes if player dies
            print("You have died {}. Thanks for playing!!".format(character.get_name()))
            print("You made it to room {}.".format(room_number))
        else:  # Executes if player completes the game
            print("Congratulations {}! You have completed the mob fighting simulator!".format(character.get_name()))
