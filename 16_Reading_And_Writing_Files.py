from sys import argv

script, filename = argv
# assigning argv for usage of f-string and input

print(f"We're going to erase {filename}.")
# f-string

print("If you don't want that, hit CTRL-C.")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")
# This line specifies what you want to do with filename (w for write)
# you HAVE to specify what you want to do with the filename if you use truncate()

print("Truncating the file. Goodbye!")
target.truncate()
# Truncate = "think of it as moving the readhead to the beginning and erasing the data"

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
# three lines of input into the text file

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# writing to the txt file


print("And finally, we close it.")
target.close()
# you should close all you files ! if not, you can LEAK files.

# running this with a .txt file: overwriting it
# also interesting: makes any file you put into the input
