from sys import exit
from flask import session
from thefuzz import fuzz
from thefuzz import process
import logging
import warnings

warnings.filterwarnings("ignore")
logging.getLogger().setLevel(logging.ERROR)


def get_choice(input, choices):
    choice, score = process.extractOne(input, choices, score_cutoff=70)
    return choice


class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


def load_room(name):
    """
    There is a potential problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)


start_room = Room(
    "Start",
    """
    Do you have it?
    The password?
    """,
)

cookie_room = Room(
    "Cookie",
    """
    ٩꒰｡•◡•｡꒱۶ congratz! go get yourself a cookie for your efforts 🍪 
    """,
)

no_cookie_room = Room(
    "No cookie",
    """
    Whoops! that is not correct! Now onto the game :)
    """,
)

main_room = Room(
    "Main",
    """
    While taking a stupid little walk for your stupid little mental health you come across a triple fork in your path.
    There is a road to the left, middle and right.
    You wonder which way to go...
    """,
)

question_mark_room_secret = Room(
    "You found the secret ending!",
    """
    Well hello there! didnt expect you here :D

    """,
)

djungelskog_room = Room(
    "Djungelskog",
    """
    You have encountered the soft and cuddly (yet quite stinky!) Djungelskog.
    He offers a hug and a soft place to lay your head for a bit.
    Will you accept his proposal?
    """,
)

cuddle_With_djungelskog = Room(
    "Cuddle",
    """
    You started to feel drowsy just thinking about leaning into his fluffy fur.
    While dozing off, Djungelskog whispers something in your ear.
    DJUNGELSKOG: The password, my dear...
    DJUNGELSKOG: It's 'PomPomPurinLovr10'
    """,
)

imposter_room = Room(
    "Imposter",
    """
    IMPOSTER FROM AMOGUS: My, my.....
    IMPOSTER FROM AMOGUS: You look quite SUSSY today!
    Oh no! The imposter thinks you are sus!
    Type 'I swear I am not sus.' to save yourself!
    """,
)

escaped_from_among = Room(
    "Escaped from the imposter",
    """
    Whew! That was like, super close.
    """,
)

you_are_sus = Room(
    "U SUS",
    """
    IMPOSTER FROM AMOGUS: NOOOO WAY!! u are toooo sus !!! 
    IMPOSTER FROM AMOGUS: did you take my fortnite card?????!!!!
    IMPOSTER FROM AMOGUS: YEET!!!
    Darn! You got thrown from the aircraft which you had no idea you were in !!
    """,
)

elongate_room = Room(
    "Elongate",
    """
    It's pretty cold in here...
    Wait, what's that?
    Elon Musk: *mumble mumble* elongate is so kewl *mumble mumble* buy tweetor *mumble mumble* stonks
    .....
    Uhm, What should we do?? HELP!!
    """,
)

elongate_punch = Room(
    "You punched Elon",
    """
    Wow! You punched him HARD! So cool!
    While Elon is unconscious, you notice a  little hole were you can barely fit through and make you way into the unknown room it led to.

    """,
)

elongate_stonks = Room(
    "You stole his stonks",
    """
    YOINK!!!
    But, now what?
    You are stuck here forever :(
    """,
)

elongate_hack = Room(
    "You hacked into his twitter account",
    """
    You grab his phone and HACK into his twitter account and DELETE IT.
    All of humanity reunites again, the ecosystem is getting better and you can feel the air getting fresher.
    No more elon. all the cringe has been eradicated in the world.
    """,
)

elon_death_room = Room(
    "Twitter cringe",
    """
    Elon YOINKS you and makes you look at every tweet that he ever wrote (they are super cringe)
    You cannot take it anymore and you faint.
    """,
)

winner_room = Room(
    "The end",
    """
    Oh you made it! I am proud of you :) 
    You saved humanity by the skin of your teeth, and you will now be remembered as a great hero.
    Good Job!
    """,
)


death = Room("death", "You failed to reach the end!")

main_room.add_paths({"up": question_mark_room_secret})

djungelskog_room.add_paths({"no": death})

imposter_room.add_paths({"I swear I am not sus.": escaped_from_among})

escaped_from_among.add_paths({"*": start_room})

elongate_punch.add_paths({"*": imposter_room})

elongate_stonks.add_paths({"*": death})

elongate_hack.add_paths({"*": winner_room})

elon_death_room.add_paths({"*": death})

if __name__ == "__main__":
    start_room()
