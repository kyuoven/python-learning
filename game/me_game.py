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

if day.lower() in ('good', 'amazing', 'great', 'fantastic','great','nice', 'acceptable', 'better than normal', 'fun'):
    print("Nice to hear!")
    print("Do you want to reflect on anything that happened today? (yes/no)")

elif day.lower() in ("bad", "not good", "shitty",'poor','terrible','depressed','unfortunate','awful'):
    print("I hope you feel better soon!")
    print("Would you like to talk to me about your day? (yes/no)")

else:
    print('I do not understand :-(')

yes_or_no = input("> ")

if yes_or_no.lower() in ("yes") :
    print("Tell me all about your day, then! :-) <3!")
    input("> ")

elif yes_or_no.lower() in ("no") :
    print("Okay! I will respect your boundaries.")

print("Another question! Did you eat yet today? (yes/no) ")

food = input("> ")

if food.lower() in ("yes") :
    print("Good job! I am proud of you, keep doing well.")
elif food.lower() in ("no") :
    print("Please have something! ( 'ω')旦~~ Eating enough is vital to be able to do things you like doing.")
    print("Like watering flowers or taking a nap! (。-ω-)zzz ")

print(f"Would you like to talk some more, {your_name}? (yes/no)")


print(f"Have a nice day further! Drink enough water and stay safe, {your_name} ! ")

input = ("> ")

