# Lexicon: Defined vacbulary of words to be used for this package.

direction_words = [
    "north",
    "south",
    "east",
    "west",
    "down",
    "up",
    "left",
    "right",
    "back",
]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]


def scan(sentence):
    words = sentence.split()
    print("in scan method" + str(words))


def direction(val):
    sentence = val
    scan(val)


def verbs(val):
    words = val.split()


def stops(val):
    words = val.split()


def nouns(val):
    words = val.split()


def numbers(val):
    words = val.split()


def errors(val):
    words = val.split()


print("Please provide a sentence.")
sentence_line = input(">")
scan(sentence_line)
print("past")

word_types = {
    "noun": ["bear", "princess", "door"],
    "verb": ["go", "run", "hide", "stop", "close", "kill", "eat"],
    "stop": ["in", "of", "at", "to", "from", "the"],
    "direction": ["up", "down", "north", "south", "east", "west", "back", "forward"],
}


def type_check(word):
    word = word.lower()
    for label, type in word_types.items():
        if word in type:
            return (label, word)


def type_identify(word):
    word = word.lower()
    return [(label, word) for label, type in word_types.items() if word in type]


def scan(sentence):
    sentence_list = sentence.split()
    for k, v in enumerate(sentence_list):
        if type_identify(v):
            sentence_list[k] = type_identify(v)[0]  # needed to add [0]
        else:
            try:
                sentence_list[k] = ("number", int(v))
            except ValueError:
                sentence_list[k] = ("error", v)
    return sentence_list

    return next(
        ((label, word) for label, type in word_types.items() if word in type), None
    )
