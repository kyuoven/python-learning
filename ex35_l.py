from sys import exit


def chicken_nuggets_room():
    print(
        "This room is full of delicious freshly fried chicken nuggies. How much do you take?"
    )

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Take some :(.")

    if how_much < 50:
        print("A fine amount, very nice! You win!")
        exit(0)
    else:
        dead("Too many chicken nuggies!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            chicken_nuggets_room()
        else:
            print("I got no idea what that means.")


def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for you life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulu_room()


def joe_room():
    print("Here you see joe, standing in the middle of the room.")
    print(
        "There is only him, accompanied by a dim swinging light dangling above him, giving the room an eerie glow."
    )
    print("You know what you have to do.")
    print("Do you ask who joe is?")

    choice = input("> ")

    if "yes" in choice:
        dead("joe mama")
    elif "no" in choice:
        start()
    else:
        print("cmon man do it for the vine")


def dead(why):
    print(why, ":( u dieded")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right, middle and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    elif choice == "middle":
        joe_room()
    else:
        dead("You stumble around the room until you starve")


start()
