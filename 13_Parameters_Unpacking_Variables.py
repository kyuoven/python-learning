from sys import argv

# from module import variable
# read the WYSS section for how to run this
(
    script,
    first,
    second,
    third,
) = argv
# script is always needed, assign variables in terminal.

print(">>> argv=", repr(argv))
# python puts arguments into a list called argv

print("The script is called:", script)
print("Your first value is", first)
print("Your second varianle is", second)
print("Your third variable is", third)
