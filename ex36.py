from sys import exit


def start():
    print("Do you have it?")
    print("The password?")

    choice = input("> ")

    if "PomPomPurinLovr10" in choice:
        print("٩꒰｡•◡•｡꒱۶ congratz! go get yourself a cookie for your efforts 🍪 ")
    else:
        restart()


def restart(silent=False):
    if not silent:
        print(
            "While taking a stupid little walk for your stupid little mental health you come across a fork in your path."
        )
        print("There's only LEFT or RIGHT.")
        print("Which path do you take?")

    choice = input("> ")

    if choice == "left":
        djungelskog_room()
    elif choice == "right":
        imposter_from_amogus_room()
    else:
        print("I don't understand, your choices are LEFT or RIGHT.")
        restart(silent=True)


def dead():
    quit


def djungelskog_room():
    print("you have encountered the soft, but kind of stinky djungelskog!")
    print("He offers you a good nights sleep.")
    print("Do you take on his offer?")

    choice = input("> ")

    if "yes" in choice:
        print(
            "djungelskog gives you a soft blanket and lets you lay your head on his tummy."
        )
        print("before nodding off you hear him say something: ")
        print("DJUNGELSKOG: 'The password...'")
        print("'...'")
        print("DJUNGELSKOG: 'It's PomPomPurinLovr10'")
    elif "no" in choice:
        print("DJUNGELSKOG: 'Why? :( Is it because I am stinky? :(('")
        print("He stretches out his fuzzy limbs in order to reach you.")
        print("Long claws portrude from his stuffy-like paws.")
        print("DJUNGELSKOG: 'Game Over' ")
        dead()


def imposter_from_amogus_room():
    print("IMPOSTER FROM AMOGUS: ' My, my... '")
    print("'Don't you look a bit SUSSY today?'")
    print("Oh no! The Imposter From Amogus thinks you are sus! ")
    print(
        "Type 'I swear I am not sus.' to make sure he doesn't throw you out of the airship!"
    )

    choice = input("> ")

    if "I swear I am not sus" in choice:
        print("You got away!")
        restart()
    else:
        print("IMPOSTER FROM AMOGUS: 'No way! You are too sus! YEET!!!!")
        print("The Imposter threw you out of the aircraft.")
        print("You died.")
        dead()


start()
