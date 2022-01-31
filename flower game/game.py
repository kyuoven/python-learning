from player import Player
from flower import Cherry_Blossom, Tulip, Rose


class Game:
    def __init__(self):
        self.player = None

    def ask_for_name(self):
        print("whats ur name")
        name = input("> ")
        if self.player is None:
            self.player = Player(name)

    def ask_which_flower(self):
        print("what flower do u want")
        fLower_types = {
            "Cherry Blossom": Cherry_Blossom,
            "Tulip": Tulip,
            "Rose": Rose,
        }

        print(fLower_types)
        what_flower = input("> ")

        if what_flower == "Cherry Blossom":
            give_flower(Cherry_Blossom)
        elif what_flower == "Tulip":
            give_flower(Tulip)
        elif what_flower == "Rose":
            give_flower(Rose)
        else:
            print("pls pick a flower")


    def give_flower(self, flower):
        self.player.flower:


