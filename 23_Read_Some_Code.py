import sys

script, encoding, error = sys.argv
# instead of import argv = import sys and then sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

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
#

# DBES: DECODE BYTES ENCODE STRINGS!
