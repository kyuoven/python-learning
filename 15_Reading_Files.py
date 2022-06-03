# from the module 'sys' import the arguement variable 'argv'
from sys import argv

# listing and assigning arguement variables
script, filename = argv
# assigning a function to a variable = to do something when typed
txt = open(filename)
# regular printing
print(f"Here's your file {filename} :")
# reading the text file
print(txt.read())
# print command and input
print("Type the filename again:")
file_again = input(">")
# open file again after having input filename
txt_again = open(file_again)
# print sample text again
print(txt_again.read())

# a lot of programming terms come from the past
# txt=open(filename) any file will be displayed as a .txt file in the terminal
