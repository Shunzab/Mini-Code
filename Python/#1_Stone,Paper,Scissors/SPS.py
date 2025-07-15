import sys
import random
from enum import Enum
import end_protocol as end

l1 = "********************"
l2 = "*                  *"
l3 = "*     Welcome!     *"

print("")
print("")

print(l1)
print(l2)
print(l3)
print(l2)
print(l1)

rounds = 0

print(input("Enter anything to play!\n"))


def Stone_Paper_Scissors():

    class SPS1(Enum):  # Couldn't use it!
        STONE = 1
        PAPER = 2
        SCISSORS = 3

    human = input(
        "\nPlease Enter: \n 1 for Stone 🥌\n 2 for Paper 📜\n 3 for Scissors ✂\n\n")

    SPS2 = ["1", "2", "3"]

    if human not in SPS2:
        print("\nPlease type a legal value.😠")
        print("")
        return Stone_Paper_Scissors()

    bot = random.choice("123")

    print("")

    print("You chose " + str(human) +
          ", and Computer chose " + str(bot) + ".")

    print("")

    # I am using Player defeat and PC victory sceneario. Suit yourself!

    if int(human) == int(bot):
        print("🤔 Tie 😅")
    elif int(human) == 1 and int(bot) == 2:
        print("🔪🪓🗡💣  Defeat! 🔪🪓🗡💣 ")
    elif int(human) == 2 and int(bot) == 3:
        print("🔪🪓🗡💣  Defeat! 🔪🪓🗡💣 ")
    elif int(human) == 3 and int(bot) == 1:
        print("🔪🪓🗡💣  Defeat! 🔪🪓🗡💣 ")
    else:
        print("🥳😎🎉🎈 Victory! 🥳😎🎉🎈 ")

    print("")

    global rounds
    rounds += 1
    print("No. of rounds: " + str(rounds))

    print("Play Again?🏏\n")

    while 1:
        replay = str(input("Enter:\n'Y' for Yes\n'N' for No\n\n"))
        listreplay = ["y", "n"]
        if replay.lower() not in listreplay:
            print("\nI didn't understand. Please try again!\n")
            continue
        else:
            break

    if replay.lower() == "y":
        print("\nGet ready fo another round! 🔰")
        return Stone_Paper_Scissors()
    else:
        print("\n🎮 Thanks for playing! 🎮")
        print("😃 Have a nice day! 😃\n\n".center(20))

    exit()


SPS = Stone_Paper_Scissors()

if __name__ == "__main__":
    SPS()
