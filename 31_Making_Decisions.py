print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

bear = input("> ")

if bear == "1":
    print("The bear eats your face off. Good job!")
elif bear == "2":
    print("The bear eats your leg off. Good job!")

else:
    print(f"Well, doing {bear} is probably better.")
    print("Bear runs away.")

print("Calculate your own insanity.")
print("1. low")
print("2. moderate")
print("3. high")     

insanity = input("> ")

if insanity == "1" or insanity == "2":
    print("Your body survives powered by a mind of jello.")
    print("Good job!")
elif insanity == "3":
    print("The insanity rots your eyes into a pool of mud.")
    print("Good job!")
else:
    print("You stumble aroound and fall on a knife on die. GG.")
