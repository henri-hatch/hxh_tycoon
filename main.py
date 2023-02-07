# Hunter x Hunter Tycoon
# Configure your own "nen ability" which is pretty much just the title + brief description and stats
# Train different stats to grow stronger
# Train the different nen trainings (such as Gyo) by increasing stats
# Do combat to train stats by comparing randomly generated stats based on a level
# Fulfill quests and unlock gear to enhance stats even more with an inventory to go with

import player

def main():
    # main function, runs it all

    playerGon = player.Player("Gon", [], "ENHANCEMENT")

    playerGon.create_ability("Stronk", "It make him stronk", "ENHANCEMENT")
    playerGon.create_ability("Stronker", "It make him stronker", "ENHANCEMENT")
    playerGon.create_ability("Stronkest", "It make him the stronkest", "ENHANCEMENT")

    playerGon.print_abilities()

if __name__ == "__main__":
    main()
