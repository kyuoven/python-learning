from player import Player
from nijntje import Nijntje


class Game:
    def __init__(self):
        self.player = None

    def ask_for_name(self):
        print("whats ur name")
        name = input("> ")
        if self.player is None:
            self.player = Player(name)


print("Miffy got up very early one day.")
print("And washed herself from head til toe.")
print("There, that's done!")

print("Press ENTER to continue...")

choice = input("...")

print("She took out the prettiest dress from her closet.")
print("And do you know why she did that?")
print("Because it is her birthday today!")

print("Press ENTER to continue...")

choice = input("...")

print("And mother and father cheered 'Happy Birthday, Miffy!' ")
print("And Miffy said: 'Thank you, today will be a nice day!' ")

print("Press ENTER to continue...")

choice = input("...")

print("When the clock hit noon, the doorbell rang...")
print("It were her friends!")

print("Press ENTER to continue...")

choice = input("...")

print("And, O, they had so much fun.")
print("They played ball on the grass, and did a lot of games.")
print("Untill it was nighttime.")

print("Press ENTER to continue...")

choice = input("...")

print("And in the evening, grandma and grandpa came to visit.")
print("They also brought a present with them.")
print("What could it be?")

print("Press ENTER to continue...")

choice = input("...")

print("A bear, a real wool bear")
print("Very sweet and also very soft.")
print("'I am going to take this one with me to bed tonight', said Nijntje.")

print("Press ENTER to continue...")

choice = input("...")

print("When mom brought Miffy and her bear to bed at night, she said:")
print("'Thank you, mama.'")
print("Today was a nice day.")
