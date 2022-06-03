# the first steps to make python more useful.
# functions are like mini-scripts


# Definfing the functions first
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
    # This function prints a bunch of argv.
    # assignign args list and printing them


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1} arg2: {arg2}")
    # This function is the same as the obne above, but formatted better
    # Formatting it like this vs. the first def is more common, and faster


def print_one(arg1):
    print(f"arg1: {arg1}")
    # This function prints only one argv


def print_none():
    print("I got nothin'.")
    # This functions prints the string only, takes no arguments


# Using the functions
print_two(
    "Zed", "Shaw"
)  # from here python will jump to the def then jumo back here and continue executing.
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# anatomy of a function:
# def function_name(any_arguments, sepereated, by_commas):
# indent-define what you want to do
