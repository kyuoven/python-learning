class Room(object):
    def __init__(self, name, description, options, title=True):
        self.name = name
        self.description = description
        self.options = options
        self.title = title
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
    """,
    """
    ☆ type in password . . .
    """,
)

cookie_room = Room(
    "Wow, a cookie!",
    """
    ٩꒰｡•◡•｡꒱۶ congratz! go get yourself a cookie for your efforts 🍪
    """,
    """
    This is the end for our journey!
    """,
    title=None,
)

no_cookie_room = Room(
    "No cookie 4 u :(",
    """
    Whoops! that is not correct! Now onto the game :)
    """,
    """
    ☆ press anything to continue
    """,
    title=None,
)

main_room = Room(
    "Your adventure begins...",
    """
    While taking a stupid little walk for your stupid little mental health you come across a triple fork in your path.
    There is a road to the left, middle and right.
    You wonder which way to go...

    """,
    """
    ☆ left
    ☆ middle
    ☆ right
    ☆ ?
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
    """
    ☆ type "I am ready" ...
    """,
    title=None,
)

djungelskog_room = Room(
    "You chose to go left",
    """
    You have encountered the soft and cuddly (yet quite stinky!) Djungelskog.
    He offers a hug and a soft place to lay your head for a bit.
    Will you accept his proposal?
    """,
    """
    ☆ yes
    ☆ no
    """,
    title=None,
)

cuddle_With_djungelskog = Room(
    "You chose to cuddle the mighty Djungelskog. This will be a nice nap",
    """
    You started to feel drowsy just thinking about leaning into his fluffy fur.
    While dozing off, Djungelskog whispers something in your ear.
    DJUNGELSKOG: The password, my dear...
    DJUNGELSKOG: It's 'PomPomPurinLovr10'
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

imposter_room = Room(
    "You chose to head right",
    """
    IMPOSTER FROM AMOGUS: My, my.....
    IMPOSTER FROM AMOGUS: You look quite SUSSY today!
    Oh no! The imposter thinks you are sus!
    """,
    """
    ☆ Type 'I swear I am not sus.' to save yourself
    """,
    title=None,
)

escaped_from_among = Room(
    "You barely escaped from the among! ",
    """
    Whew! That was like, super close.
    Let's continue.
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

you_are_sus = Room(
    "U SUS!!!!!!",
    """
    IMPOSTER FROM AMOGUS: NOOOO WAY!! u are toooo sus !!!
    IMPOSTER FROM AMOGUS: did you take my fortnite card?????!!!!
    IMPOSTER FROM AMOGUS: YEET!!!
    Darn! You got thrown from the aircraft which you had no idea you were in !!
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

elongate_room = Room(
    "You chose the middle path",
    """
    It's pretty cold in here...
    Wait, what's that?
    Elon Musk: *mumble mumble* elongate is so kewl *mumble mumble* buy tweetor *mumble mumble* stonks
    .....
    Uhm, What should we do?? HELP!!
    """,
    """
    ☆ punch him in the FACE
    ☆ hack him
    ☆ steal his stonks
    """,
    title=None,
)

elongate_punch = Room(
    "You chose to punch Elon",
    """
    Wow! You punched him HARD! So cool!
    While Elon is unconscious, you notice a  little hole were you can barely fit through and make you way into the unknown room it led to.
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

elongate_stonks = Room(
    "You stole his stonks",
    """
    YOINK!!!
    But, now what?
    You are stuck here forever :(
    """,
    """
    ☆ You cannot continue.
    """,
    title=None,
)

elongate_hack = Room(
    "You hacked into his twitter account",
    """
    You grab his phone and HACK into his twitter account and DELETE IT.
    All of humanity reunites again, the ecosystem is getting better and you can feel the air getting fresher.
    No more elon. all the cringe has been eradicated in the world.
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

elon_death_room = Room(
    "Watch out!",
    """
    Elon YOINKS you and makes you look at every tweet that he ever wrote (they are super cringe)
    You cannot take it anymore and you faint.
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

winner_room = Room(
    "This is the end. Is it?",
    """
    Oh you made it! I am proud of you :)
    You saved humanity by the skin of your teeth, and you will now be remembered as a great hero.
    Good Job!
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

i_dont_understand_room = Room(
    "I didn't understand that",
    """
    Sorry! Could you try something else?
    """,
    """
    ☆ type anything to continue . . .
    """,
    title=None,
)

death = Room(
    "You died, how sad",
    """
    You failed to reach the end :( noob
    """,
    """
    ☆ type anything to continue ...
    """,
    title=None,
)

START = "start_room"

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

cuddle_With_djungelskog.add_paths({"*": start_room})

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
