from sys import exit


def intro_to_game():
    print("It's a calm friday night at your job in the grocery store.")
    print("People are busy checking their shopping lists and being full of themselves.")
    print(
        "The dusty clock on your left is chipping away at the 2 hours and 40 minutes left on your shift."
    )
    print("Where do you want to look?")
    print(" > Your desk")
    print(" > To the left")
    print(" > In front of you")
    print(" > To the right")
    print(" > Behind you")
    print(" > In the closet")
    print(" > In the register")
    print(" > Outside")

    choice = input(">... ").lower()

    if choice == "your desk":
        print(
            "There's a five cent coin and a paperclip on there, but besides that there's nothing interesting."
        )
        restart()

    elif choice == "to the left":
        print("That's where the freezer isle is.")
        print(
            "You can't see much from your seat, but you can make out some frozen fries and patties."
        )
        print("Now you are wondering what you are going to eat later.")
        restart()

    elif choice == "in front of you":
        print("There is no one in front of you, even the isles are empty.")
        print("Sooner or later, there will be people here.")
        restart()

    elif choice == "to the right":
        print("That's where the entrance is.")
        print("And also, the toys isle. Many dreams were crushed there.")
        restart()

    elif choice == "behind you":
        print(" :) ")
        dead()

    elif choice == "in the closet":
        print("Your snackbar and jacket are in here.")
        print("As well as your bag, which has your important stuff in it.")
        print("Like condoms and stuff.")
        restart()

    elif choice == "in the register":
        print("What? You trynna steal?")
        print("I would strongly advise against that, there are cameras pointed at you.")
        fired()

    elif choice == "outside":
        print(
            "The sun is starting to set, but the rain from earlier is stopping at last."
        )
        print("You hope to be able to bike home without any problems.")
        men_entering()

    else:
        print("What? Pick a choice.")


def dead():
    print("you dieded.")
    quit()


def fired():
    print("U GOT FIRED!!!111!!!!111!1!!!")
    dead()


def men_entering():
    print("Two men in suits enter the building.")
    print("And they are heading straight for the register.")
    print("You panic.")
    print("What's your plan?")
    print(" > Run away")
    print(" > Stay calm")

    choice = input(">... ").lower()

    if choice == "run away":
        print("The men in suits thought you were suspicious and shot you on site")
        dead()
    elif choice == "stay calm":
        print("Good job, there was no reason to get paranoid anyway.")
        men_at_register()


def men_at_register():
    print("Man one: 'We're gonna need to see your goods.' ")
    print("Y/N: my goods?")
    print("Man two: 'Yeah, hand em over. And fast.' ")

    print("Uhmm this isn't planned. Let me check the files.")
    print("Man one: ḧḕẏ?? ẇḧḀṮ ḭṠ ḠṏḭṆḠ ṏṆ/??-")
    print("Man two: What tḧḕ ḟṳḉḲ-")
    print("SUCCESSFULLY DELETED CHAR_ALEX")
    print("SUCCESSFULLY DELETED CHAR_PHIL")

    print("Y/N: ... ")
    win()


def win():
    print("congrats! only one more step to go to win this silly game")
    print("it is a simple yes or no question, are you ready? :)")
    print(" > yes ")
    print(" > no ")

    choice = input(">... ").lower()

    if choice == "yes":
        print("good! u win")

    elif choice == "no":
        print("oh, so sad :(")
        dead()
