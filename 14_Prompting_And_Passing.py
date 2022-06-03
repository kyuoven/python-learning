from sys import argv

script, user_name = argv
prompt = f"{script} ({user_name})>"

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"How old are you {user_name}?")
age = input(prompt)

print(f"You're {int(age)} What kind of computer do you have?")
computer = input(prompt)

print(
    f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
"""
)

# argvs takes command line arguments
# script (ex14) and {user_name} shows up before the input section in the terminal
# int: coverts a specified value into an integer number.
