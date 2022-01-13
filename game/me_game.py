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

day = input("> ")

if day.lower() in ('good', 'amazing', 'great'):
    print("Nice to hear!")
    print("Do you want to reflect on anything that happened today? (yes/no)")

elif day.lower() in ("bad", "not good", "shitty"):
    print("I hope you feel better soon!")
    print("Would you like to talk to me about your day? (yes/no)")

else:
    print('I do not understand :-(')

yes_or_no = input("> ")

if yes_or_no.lower() in ("yes"):
    print("Tell me all about your day, then! :-) <3!")

elif yes_or_no.lower() in ("no"):
    print("Okay! I will respect your boundaries.")

