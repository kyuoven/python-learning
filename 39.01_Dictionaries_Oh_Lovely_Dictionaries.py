# 0-10 of how much i like it
foods_dict = {
    # "key": "value",
    "rice": 8,
    "pudding": 6,
    "soup": 5,
    "wraps": 7,
    "pulled pork": 9.5,
    "noodles": 7,
    "salame": 6,
    "cheese": 7,
    "bread": 8,
}

# same thing here
drinks_dict = {
    "cola": 9,
    "fanta": 8,
    "coffee": 10,
    "water": 5,
    "protein shake": 10,
}

# adding some more stuff
foods_dict["dried vegetables"] = 9  # dict[key] =  value
drinks_dict["tea"] = 9

# now the dictionary has more things
print(foods_dict)
print(drinks_dict)

# "Instead of only being able to use positions, you can use almost anything to access the elements within a dictionary.
# This lets you treat a dict like it's a database for storing and organizing data."

# using the foods_dict
print("\n")
print("Let's rate some foods:")
print("\n")
print("The score i give rice is:", foods_dict["rice"])  # print("message:", dict[key])
print("The score i give pudding is:", foods_dict["pudding"])
print("The score i give soup is:", foods_dict["soup"])
print("The score i give wraps is:", foods_dict["wraps"])
print("The score i give pulled pork is:", foods_dict["pulled pork"])
print("The score i give noodles is:", foods_dict["noodles"])
print("The score i give salame is:", foods_dict["salame"])
print("The score i give cheese is:", foods_dict["cheese"])
print("The score i give bread is:", foods_dict["bread"])
print("And let's not forget!")
print("The score i give dried vegetables is:", foods_dict["dried vegetables"])

print("\n")
print("Now let's rate some drinks:")
print("\n")
print("The score i give cola is:", drinks_dict["cola"])
print("The score i give fanta is:", drinks_dict["fanta"])
print("The score i give coffee is:", drinks_dict["coffee"])
print("The score i give water is:", drinks_dict["water"])
print("The score i give protein shake is:", drinks_dict["protein shake"])
print("And let's not forget!")
print("The score i give tea is:", drinks_dict["tea"])

print("\n")
print("\t i rated a lot of food and drinks! Time for some food and drinks")

print("\n")
print("Rate them yourself!")
print("Here:")

print("\n")

print(foods_dict.keys())  # .keys() returns the keys of a dictionary
print(drinks_dict.keys())
