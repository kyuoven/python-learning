# 2022-05-23: added gateway_to_hell() adn connected it to imposter_from_amogus_room(), tweaked some other lines


from sys import exit


def start():
    print("Do you have it?")
    print("The password?")

    choice = input("> ")

    if "PomPomPurinLovr10" in choice:
        print("٩꒰｡•◡•｡꒱۶ congratz! go get yourself a cookie for your efforts 🍪 ")
    else:
        print("Whoops! That's not it buddy. Try again :)")
        restart()


def restart(silent=False):
    if not silent:
        print(
            "While taking a stupid little walk for your stupid little mental health you come across a fork in your path."
        )
        print("There's only LEFT, MIDDLE or RIGHT.")
        print("Which path do you take?")

    choice = input("> ")

    if choice == "left":
        djungelskog_room()
    elif choice == "right":
        imposter_from_amogus_room()
    elif choice == "middle":
        gateway_to_hell()
    else:
        print("I don't understand, your choices are LEFT or RIGHT.")
        restart(silent=True)


def dead():
    quit()


def winning():
    print("super! u won!")
    quit()


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

        input("> ")

        print("In your last moments.. u see the image ... copy paste pls...")
        print("https://i1.sndcdn.com/artworks-yCyieQL117W6vBo2-KvzneQ-t500x500.jpg")
        dead()


def gateway_to_hell():
    print("Well here you are.")
    print("It's quite cold here, isn't it?")

    choice = input("> ")

    print("Hmmmm.... Something seems off.....")
    print("..........")
    print("Wait! What is that???!!!")
    print(
        "Elon Musk: *mumble mumble* elongate is so kewl *mumble mumble* buy tweetor *mumble mumble* stonks"
    )
    print("................")
    print("Uhm what should we do? Help!")

    choice = input("> ")

    if "punch him in the FACE" in choice:
        print("DAAAMN. u punched him HARD!!!! ")
        print(
            "While cringelord elon is unconscious, you slipped away and ran towards the ford in the path you came across earlier."
        )

        input("> ")

        imposter_from_amogus_room()

    elif "steal his stonks":
        print("YOINK!!!!")
        print("... and now what?")
        print("You are stuck here now :(")
        quit()

    elif "hack his twitter":
        print("You grab his phone and HACK into his twitter account and DELETE IT.")
        print(
            "All of humanity reunites again, the ecosystem is getting better and you can feel the air getting fresher."
        )
        print("no more elon. all the cringe has been eradicated in the world.")
        winning()

    else:
        print(
            "Elon YOINKS you and makes you look at every tweet that he ever wrote (they are super cringe)"
        )
        print("You can't take it anymore and faint")
        dead()


if __name__ == "__main__":
    start()
