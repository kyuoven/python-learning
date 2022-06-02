import contextlib

dictionary = {"name": "l", "value": "0"}
# This line defines a variable called dictionary containing a dictionary.
# The dictionary has two keys 'name' and 'value' and their values are 'l' and '0' respectively.
def test(dictionary, name, value=None):
    # This line defines the function called 'test' and has three parameters: 'poop' , 'name', and 'value'.
    # with value having a default value of None.
    # All three are variables -> act like variables in the scope of the function
    return dictionary.get(name, value)
    # if the name key is found in a dictionary it returns its corresponding value
    # else it will return the value parameter from the test function
    # .get only works with dictionaries


with contextlib.suppress(NameError):
    print("test 1")
    print(test({"a": 10, "b": 201}, a))  # error -> NameError

print("test 2")
print(test({"a": 10, "b": 201}, "a"))  # 10 -> 10

print("test 3")
print(test({"a": 10, "b": 201}, "c"))  # NameError -> None

print("test 4")
print(test({"a": 10, "b": 201}, "b"))  # 201 -> 201

print("test 5")
print(test({"a": 10, "b": 201}, "b", 341))  # 201 -> 201

print("test 6")
print(test({"a": 10, "b": 201}, "f", 341))  # None -> 341

print("test 7")
print(test({"a": 10, "b": 201}, g, 341))  # NameError -> NameError
