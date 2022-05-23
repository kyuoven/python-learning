class Player:
    def asking_player_name(self):
        print("What name do you go by?")

        self.name = input(">... ")

        print(f"{self.name}... ok!")
        print("You're all set :)")


def the_sun_is_shining():
    print("Huh, it looks like its a nice day today")
    print("The sun is shining, there's a soft breeze tickling the grass.")
    print("Would you like to go out? (YES/NO)")

    choice = input(">... ").lower

    if choice == "Yes":
        print("Sounds like a nice idea.")
        winning()

    elif choice == "No":
        print("Okay, it was going to rain later anyway")
        sun_is_hiding()

    else:
        print("it doesn't matter")
        print("because")


def sun_is_hiding():
    print("The sun is no longer shining as proudly as before.")
    print("What happened, Mr. Sun?")
    print("...")
    print("Oh forget it, let's just stay inside and read a book.")

    print("...")

    print("What book do you want to read?")
    print("> Alice in Wonderland")
    print("> The fault in our stars")
    print("> The very hungry caterpillar")
    print("> Stare into the void")
    print("> Nothing, let's just go to bed")

    choice = input(">... ").lower

    if choice == "alice in wonderland":
        print("CHAPTER I")
        print("Down the rabbit hole.")
        print(
            "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'"
        )
        print(
            "So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. "
        )

        print("...")
        print("Hey, you stil there? (Y/N)")

        choice = input(">... ").lower

        if choice == "yes":
            print("no ur not")
        elif choice == "no":
            print("good, the book was getting boring anyway.")

    elif choice == "the fault in our stars":
        print(
            "Late in the winter of my seventeenth year, my mother decided I was depressed, presumably because I never left the house, spent quite a lot of time in bed, read the same book over and over, ate infrequently, and devoted quite a bit of my abundant free time to thinking about death."
        )
        print("...")
        print("Hey, you stil there? (Y/N)")

        choice = input(">... ").lower

        if choice == "yes":
            print("no ur not")
        elif choice == "no":
            print("good, the book was getting boring anyway.")

    elif choice == "the hungry caterpillar":
        print("In the light of the moon, a little egg lay on a leaf.")
        print(
            "One sunday morning the warm sun came up and pop! -out of the egg came a tiny and very hungry caterpillar."
        )
        print("He started to look for some food.")
        print("On monday he ate through one apple. but he was still hungry.")

        print("...")
        print("Hey, you stil there? (Y/N)")

        choice = input(">... ").lower

        if choice == "yes":
            print("no ur not")
        elif choice == "no":
            print("good, the book was getting boring anyway.")

    elif choice == "nothing, let's just go to bed":
        print("okay.")
        no_fun_today()

    elif choice == "stare into the void":
        print("Huh, i havent heard of that book.")

        print("What book do you want to read?")
        print("> Alice in Wonderland")
        print("> The fault in our stars")
        print("> The very hungry caterpillar")
        print("> Nothing, let's just go to bed")

    else:
        print("pls pick a book")

        choice = input(">... ").lower

        if choice == "alice in wonderland":
            print("CHAPTER I")
            print("Down the rabbit hole.")
            print(
                "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, `and what is the use of a book,' thought Alice `without pictures or conversation?'"
            )
            print(
                "So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her. "
            )

            print("...")
            print("Hey, you stil there? (Y/N)")

            choice = input(">... ").lower

            if choice == "yes":
                print("no ur not")
            elif choice == "no":
                print("good, the book was getting boring anyway.")

        elif choice == "the fault in our stars":
            print(
                "Late in the winter of my seventeenth year, my mother decided I was depressed, presumably because I never left the house, spent quite a lot of time in bed, read the same book over and over, ate infrequently, and devoted quite a bit of my abundant free time to thinking about death."
            )
            print("...")
            print("Hey, you stil there? (Y/N)")

            choice = input(">... ").lower

            if choice == "yes":
                print("no ur not")
            elif choice == "no":
                print("good, the book was getting boring anyway.")

        elif choice == "the hungry caterpillar":
            print("In the light of the moon, a little egg lay on a leaf.")
            print(
                "One sunday morning the warm sun came up and pop! -out of the egg came a tiny and very hungry caterpillar."
            )
            print("He started to look for some food.")
            print("On monday he ate through one apple. but he was still hungry.")

            print("...")
            print("Hey, you stil there? (Y/N)")

            choice = input(">... ").lower

            if choice == "yes":
                print("no ur not")
            elif choice == "no":
                print("good, the book was getting boring anyway.")

        else:
            print("idk what u want from me")


def winning():
    print("Yay! today was nice, let's celebrate with some ice cream.")


def no_fun_today():
    print("You had no fun today and died of boredom. the end.")


player = Player()
player.asking_player_name()

the_sun_is_shining()
sun_is_hiding()
