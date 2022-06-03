from sys import argv

# from module 'sys' import argument variable

script, input_file = argv
# assigning argvs

# f is file
def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f=", f)
    # not copying the file, we are passing it by reference


def rewind(f):
    f.seek(0)
    # a way to rewind (comes from mainframe tape days)


def print_a_line(line_count, f):
    print(line_count, f.readline())
    # will only read one line


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)
# one line

current_line = current_line + 1
print_a_line(current_line, current_file)
# becomes two lines

current_line = current_line + 1
print_a_line(current_line, current_file)
# becomes three lines
