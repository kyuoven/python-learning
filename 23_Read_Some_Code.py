import sys

script, encoding, error = sys.argv
# instead of import argv = import sys and then sys.argv
# script, encoding and error for argv
# from the module 'sys' use these variables from the list


def main(language_file, encoding, errors):  # script encoding errors
    # This line defines a function called main, which takes 3 parameters: language_file, encoding and errors.
    line = language_file.readline()
    # This line assigns a line of string readline from language_file to the line variable

    if line:  # if there are any lines
        # first if! what it does:
        print_line(line, encoding, errors)  # call print line
        return main(language_file, encoding, errors)
        # calling main inside main? combining stuff. you can call any function inside a function.
        # calling main inside main= creating a loop until there are no lines to read/print !
        # if no line, the if clause gets skipped


def print_line(
    line, encoding, errors
):  # takes the line you want to print, the utf encoding and how to handle errors - it strips it
    # encoding and decoding unicode
    print(">>>> print_line", repr(line), encoding, errors)
    next_lang = line.strip()  # strips the  line
    # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end)
    # characters (space is the default leading character to remove)
    # example: strip(abc) would strip the string of letters that correspond with a, b and c.
    # syntax: string.strip([chars])
    raw_bytes = next_lang.encode(encoding, errors=errors)  # encoding the line
    # errors = errors? gets passed to the function as an extra option named errors
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # decoded raw bytes

    print(raw_bytes, "<===>", cooked_string)
    print("<<<< exit print_line")

    # prints it out


languages = open("languages.txt", encoding="utf-8")
# open languages file, force the utf-8

main(languages, encoding, error)
# 'main' gets called here and runs it

# DBES: DECODE BYTES ENCODE STRINGS!
