def add(a, b):
    print(f"ADDING {a} + {b} ")
    return a + b


def subtract(a, b):
    print(f"SUBTRACTING {a} - {b} ")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b} ")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b} ")
    return a / b


print("Let's do some math with just functions!")

age = add(
    30, 5
)  # calling add, printing out a, b and returns it. then variable 'age' has 35.
print(">>>> age=", age)
height = subtract(78, 4)  # same thing - subtracts
print(">>>> height=", height)
weight = multiply(90, 2)  # same thing - multiplies
print(">>>> weight=", weight)
iq = divide(100, 2)  # same thing - divides
print(">>>> iq=", iq)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

# iq = 2 / weight, * height, - age
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, "Can you do it by hand")

# ❯ python
# Python 3.8.10 (default, Nov 26 2021, 20:14:08)
# [GCC 9.3.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> # what =  add(age, subtract(height, multiply(weight, divide(iq, 2))))
# >>> iq = 50
# >>> weight = 180
# >>> height = 74
# >>> age = 35
# >>> iq / 2
# 25.0
# >>> # what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# >>>  # what = add(age, subtract(height, multiply(weight, divide(25)))
# >>> weight *25
# 4500
# >>>  # what = add(age, subtract(height, 4500))
# >>> height - 4500
# -4426
# >>>  # what = add(-4426)
# >>> what = age + 4426
# >>> what
# 4461
# >>> what = age + -4426
# >>> what
# -4391
# >>>
