# wrap it wround your head: if you can do one thing, you can probably do it with another thing in python
# pay attention to errors: even if the output seems strange

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two from one line, how?
in_file = open(from_file)
print(">>>> in_file=", repr(in_file))
# repr() gives you the representation, the raw python version of it
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
# always close your files- for small exercises like this it's not as important,
# but you should get in the habit of doing this.
