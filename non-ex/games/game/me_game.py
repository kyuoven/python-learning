GOOD_DAY = [
    "good",
    "amazing",
    "great",
    "fantastic",
    "great",
    "nice",
    "acceptable",
    "better than normal",
    "fun",
    "it was good",
    "it was great",
    "it was okay",
    "it was ok",
    "fine",
]

BAD_DAY = [
    "bad",
    "not good",
    "shitty",
    "poor",
    "terrible",
    "depressed",
    "unfortunate",
    "awful",
]


print("Hi.")
print("Press 'enter' to continue.")

input("> ")

print("Welcome to Me!")
print("Press 'enter' to continue.")

input("> ")

print(f"What is your name?")

your_name = input("> ")

print(f"Lovely! What a nice name you have, {your_name}. :-)")
print(f"How was your day today, {your_name}?")

understood = False

while not understood:
    day = input("> ")
    if day.lower() in GOOD_DAY:
        print("Nice to hear!")
        print("Do you want to reflect on anything that happened today? (yes/no)")
        understood = True

    elif day.lower() in BAD_DAY:
        print("I hope you feel better soon!")
        print("Would you like to talk to me about your day? (yes/no)")
        understood = True

    else:
        print("I do not understand :-(")

understood = False

while not understood:
    yes_or_no = input("> ")

    if yes_or_no.lower() in ("yes"):
        print("Tell me all about your day, then! :-) <3!")
        input("> ")
        understood = True

    elif yes_or_no.lower() in ("no"):
        print("Okay! I will respect your boundaries.")
        understood = True

print("Another question! Did you eat yet today? (yes/no) ")

understood = False
while not understood:
    food = input("> ")
    if food.lower() in ("yes"):
        print("Good job! I am proud of you, keep doing well.")
        break

    elif food.lower() in ("no"):
        print(
            "Please have something! ( 'ω')旦~~ Eating enough is vital to be able to do things you like doing."
        )
        print("Like watering flowers or taking a nap! (。-ω-)zzz ")
        break

understood = False
while not understood:
    print(f"Would you like to talk some more, {your_name}? (yes/no)")
    moretalk_yes_no = input("> ")

    if moretalk_yes_no.lower() in ("yes"):
        print("Okay („ᵕᴗᵕ„)")
        print(
            f"Is there anything in specific you would want to talk about, {your_name}? "
        )
        understood = True
    elif moretalk_yes_no.lower() in ("no"):
        print("TODO Lucas")
        understood = True
    else:
        print("I do not understand")

print(f"Have a nice day further! Drink enough water and stay safe, {your_name} ! ")

input = "> "

quit()
