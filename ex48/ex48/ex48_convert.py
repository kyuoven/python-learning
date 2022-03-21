def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


# You put the code you want to “try” inside the try block, and then you put the
# code to run for the error inside the except. In this case, we want to “try” to
# call int() on something that might be a number. If that has an error, then we
# “catch” it and return None.
