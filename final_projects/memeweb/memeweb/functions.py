class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        default = self.paths.get("*")
        return self.paths.get(direction, default)

    def add_paths(self, paths):
        self.paths.update(paths)


def load_room(name):
    # This line defines the function 'load_room' which has one parameter.
    return globals().get(name)
    # This line returns the value of the key name if it is found in globals (dict)


def name_room(room):
    for key, value in globals().items():
        if value == room:
            return key


def test():
    return globals()


start_room = Room(
    "The start",
    """
    Do you have it?
    The password?

    \n> type in password . . .

    """,
)

cookie_room = Room(
    "Wow, a cookie!",
    """
    ٩꒰｡•◡•｡꒱۶ congratz! go get yourself a cookie for your efforts 🍪
    """,
)

no_cookie_room = Room(
    "No cookie 4 u :(",
    """
    Whoops! that is not correct! Now onto the game :)
    """,
)

main_room = Room(
    "Your adventure begins...",
    """
    While taking a stupid little walk for your stupid little mental health you come across a triple fork in your path.
    There is a road to the left, middle and right.
    You wonder which way to go...

    \n> left
    \n> middle
    \n> right
    \n> ?
    """,
)

question_mark_room_secret = Room(
    "You found the secret ending!",
    """
    Well hello there! didnt expect you here :D
    Enjoy your time in this humble abode!
    ...
    Whenever you are ready, just type "I am ready" to continue playing.
    Stay safe, stay sane and hydrated.
    <3

    """,
)

djungelskog_room = Room(
    "You chose to go left",
    """
    You have encountered the soft and cuddly (yet quite stinky!) Djungelskog.
    He offers a hug and a soft place to lay your head for a bit.
    Will you accept his proposal?

    \n> yes
    \n> no
    """,
)

cuddle_With_djungelskog = Room(
    "You chose to cuddle the mighty Djungelskog. This will be a nice nap",
    """
    You started to feel drowsy just thinking about leaning into his fluffy fur.
    While dozing off, Djungelskog whispers something in your ear.
    DJUNGELSKOG: The password, my dear...
    DJUNGELSKOG: It's 'PomPomPurinLovr10'

    \n> type anything to continue . . .
    """,
)

imposter_room = Room(
    "You chose to head right",
    """
    IMPOSTER FROM AMOGUS: My, my.....
    IMPOSTER FROM AMOGUS: You look quite SUSSY today!
    Oh no! The imposter thinks you are sus!

    \n > Type 'I swear I am not sus.' to save yourself
    """,
)

escaped_from_among = Room(
    "You barely escaped from the among! ",
    """
    Whew! That was like, super close.
    Let's continue.

    \n> type anything to continue . . .
    """,
)

you_are_sus = Room(
    "U SUS!!!!!!",
    """
    IMPOSTER FROM AMOGUS: NOOOO WAY!! u are toooo sus !!!
    IMPOSTER FROM AMOGUS: did you take my fortnite card?????!!!!
    IMPOSTER FROM AMOGUS: YEET!!!
    Darn! You got thrown from the aircraft which you had no idea you were in !!

    \n> type anything to continue . . .
    """,
)

elongate_room = Room(
    "You chose the middle path",
    """
    It's pretty cold in here...
    Wait, what's that?
    Elon Musk: *mumble mumble* elongate is so kewl *mumble mumble* buy tweetor *mumble mumble* stonks
    .....
    Uhm, What should we do?? HELP!!

    \n> punch him in the FACE
    \n> hack him
    \n> steal his stonks
    \n
    """,
)

elongate_punch = Room(
    "You chose to punch Elon",
    """
    Wow! You punched him HARD! So cool!
    While Elon is unconscious, you notice a  little hole were you can barely fit through and make you way into the unknown room it led to.

    \n> type anything to continue . . .

    """,
)

elongate_stonks = Room(
    "You stole his stonks",
    """
    YOINK!!!
    But, now what?
    You are stuck here forever :(

    \n> You cannot continue.
    """,
)

elongate_hack = Room(
    "You hacked into his twitter account",
    """
    You grab his phone and HACK into his twitter account and DELETE IT.
    All of humanity reunites again, the ecosystem is getting better and you can feel the air getting fresher.
    No more elon. all the cringe has been eradicated in the world.

    \n> type anything to continue . . .
    """,
)

elon_death_room = Room(
    "Watch out!",
    """
    Elon YOINKS you and makes you look at every tweet that he ever wrote (they are super cringe)
    You cannot take it anymore and you faint.

    \n> type anything to continue . . .
    """,
)

winner_room = Room(
    "This is the end. Is it?",
    """
    Oh you made it! I am proud of you :)
    You saved humanity by the skin of your teeth, and you will now be remembered as a great hero.
    Good Job!

    \n> type anything to continue . . .
    """,
)

i_dont_understand_room = Room(
    "I didn't understand that",
    """
    Sorry! Could you try something else?

    \n> type anything to continue . . .
    """,
)


START = "start_room"

death = Room("You died, how sad", "You failed to reach the end :( noob")

cookie_room.add_paths({"*": main_room})

i_dont_understand_room.add_paths({"*": main_room})

main_room.add_paths({"left": djungelskog_room})

main_room.add_paths({"middle": elongate_room})

main_room.add_paths({"right": imposter_room})

main_room.add_paths({"up": question_mark_room_secret})

question_mark_room_secret.add_paths({"I am ready": start_room})

main_room.add_paths({"*": i_dont_understand_room})

elongate_room.add_paths({"punch him in the FACE": elongate_punch})

elongate_room.add_paths({"hack him": elongate_hack})

elongate_room.add_paths({"steal his stonks": elongate_stonks})

elongate_room.add_paths({"*": i_dont_understand_room})

djungelskog_room.add_paths({"yes": cuddle_With_djungelskog})

djungelskog_room.add_paths({"no": death})

djungelskog_room.add_paths({"*": i_dont_understand_room})

imposter_room.add_paths({"I swear I am not sus.": escaped_from_among})

imposter_room.add_paths({"*": you_are_sus})

escaped_from_among.add_paths({"*": start_room})

you_are_sus.add_paths({"*": death})

elongate_punch.add_paths({"*": imposter_room})

elongate_stonks.add_paths({"*": death})

elongate_hack.add_paths({"*": winner_room})

elon_death_room.add_paths({"*": death})

question_mark_room_secret.add_paths({"I am ready.": main_room})

start_room.add_paths({"PomPomPurinLovr10": cookie_room})

start_room.add_paths({"*": no_cookie_room})

no_cookie_room.add_paths({"*": main_room})

winner_room.add_paths({"*": main_room})

death.add_paths({"*": start_room})

if __name__ == "__main__":
    start_room
