i = 0
food = ["banana"]

while i < 10:
    print(f"And here we have {i}")
    food.append(i)

    i = i + 1
    print("Food now:", food)
    print(f"Now we have {i}")

print("the food:")

for yummy in food:
    print(yummy)
